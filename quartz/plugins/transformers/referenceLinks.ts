import { Root } from "hast"
import { visit } from "unist-util-visit"
import { QuartzTransformerPlugin } from "../types"

type HastNode = Root["children"][number]

function getText(node: HastNode): string {
  if (node.type === "text") {
    return node.value
  }

  if (node.type === "element" && node.children) {
    return node.children.map((child) => getText(child as HastNode)).join("")
  }

  return ""
}

function addReferenceIds(node: HastNode, counter: { value: number }) {
  if (node.type !== "element") {
    return
  }

  if (node.tagName === "li") {
    counter.value += 1
    node.properties = { ...(node.properties ?? {}), id: `ref-${counter.value}` }
  }

  if (node.tagName === "p") {
    const first = node.children?.[0]
    if (first?.type === "text") {
      const match = first.value.match(/^(\d+)\.\s/)
      if (match) {
        node.properties = { ...(node.properties ?? {}), id: `ref-${match[1]}` }
      }
    }
  }

  for (const child of node.children ?? []) {
    addReferenceIds(child as HastNode, counter)
  }
}

function addCitationLinks(node: HastNode) {
  if (node.type !== "element" || !node.children) {
    return
  }

  if (["a", "code", "pre", "script", "style"].includes(node.tagName)) {
    return
  }

  for (let i = 0; i < node.children.length; i += 1) {
    const child = node.children[i]
    if (child.type === "text") {
      const text = child.value
      const regex = /\[(\d+)\]/g
      let lastIndex = 0
      let match: RegExpExecArray | null = null
      const replacement: HastNode[] = []

      while ((match = regex.exec(text)) !== null) {
        if (match.index > lastIndex) {
          replacement.push({ type: "text", value: text.slice(lastIndex, match.index) } as HastNode)
        }
        replacement.push({
          type: "element",
          tagName: "a",
          properties: {
            href: `#ref-${match[1]}`,
            className: ["footnote-ref"],
            dataNoPopover: true,
          },
          children: [{ type: "text", value: match[0] }],
        } as HastNode)
        lastIndex = regex.lastIndex
      }

      if (replacement.length > 0) {
        if (lastIndex < text.length) {
          replacement.push({ type: "text", value: text.slice(lastIndex) } as HastNode)
        }
        node.children.splice(i, 1, ...replacement)
        i += replacement.length - 1
      }
    } else {
      addCitationLinks(child as HastNode)
    }
  }
}

export const ReferenceLinks: QuartzTransformerPlugin = () => {
  return {
    name: "ReferenceLinks",
    htmlPlugins() {
      return [
        () => {
          return (tree: Root) => {
            if (!tree.children?.length) {
              return
            }

            const referenceHeadingIndexes: number[] = []
            tree.children.forEach((node, index) => {
              if (node.type === "element" && node.tagName === "h2") {
                if (getText(node as HastNode).trim().toLowerCase() === "references") {
                  referenceHeadingIndexes.push(index)
                }
              }
            })

            if (referenceHeadingIndexes.length === 0) {
              return
            }

            const referencesIndex = referenceHeadingIndexes[referenceHeadingIndexes.length - 1]
            const referenceHeader = tree.children[referencesIndex]
            if (referenceHeader.type === "element") {
              referenceHeader.properties = {
                ...(referenceHeader.properties ?? {}),
                id: "references",
              }
            }

            for (let i = 0; i < referencesIndex; i += 1) {
              addCitationLinks(tree.children[i] as HastNode)
            }

            const counter = { value: 0 }
            for (let i = referencesIndex + 1; i < tree.children.length; i += 1) {
              const node = tree.children[i]
              if (node.type === "element" && node.tagName === "h2") {
                break
              }
              addReferenceIds(node as HastNode, counter)
            }
          }
        },
      ]
    },
  }
}
