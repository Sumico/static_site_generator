import unittest

from blocks import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_heading,
    block_type_paragraph,
    block_type_unordered_list,
    block_type_ordered_list,
    block_type_quote,
    block_type_code,
    document_to_html,
)


class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown_text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item
"""
        expected_blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is a list item\n* This is another list item",
        ]
        self.assertEqual(markdown_to_blocks(markdown_text), expected_blocks)

    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)

    def test_block_to_block_type_paragraph(self):
        block = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_block_to_block_type_unordered_list(self):
        block = "* This is a list item\n* This is another list item"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)

    def test_block_to_block_type_ordered_list(self):
        block = "1. This is a list item\n2. This is another list item"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)

    def test_block_to_block_type_quote(self):
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)

    def test_block_to_block_type_code(self):
        block = "```python\nprint('Hello, world!')\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)

    def test_block_to_block_type_paragraph_start_with_number(self):
        block = "1. This is a list item\n2. This is another list item\nThis is not a list item"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_document_to_html(self):
        markdown_text = """# The Unparalleled Majesty of "The Lord of the Rings"

[Back Home](/)

![LOTR image artistmonkeys](/images/rivendell.png)

> "I cordially dislike allegory in all its manifestations, and always have done so since I grew old and wary enough to detect its presence.
> I much prefer history, true or feigned, with its varied applicability to the thought and experience of readers.
> I think that many confuse 'applicability' with 'allegory'; but the one resides in the freedom of the reader, and the other in the purposed domination of the author."

In the annals of fantasy literature and the broader realm of creative world-building, few sagas can rival the intricate tapestry woven by J.R.R. Tolkien in *The Lord of the Rings*. You can find the [wiki here](https://lotr.fandom.com/wiki/Main_Page).

## Introduction

This series, a cornerstone of what I, in my many years as an **Archmage**, have come to recognize as the pinnacle of imaginative creation, stands unrivaled in its depth, complexity, and the sheer scope of its *legendarium*. As we embark on this exploration, let us delve into the reasons why this monumental work is celebrated as the finest in the world.

## A Rich Tapestry of Lore

One cannot simply discuss *The Lord of the Rings* without acknowledging the bedrock upon which it stands: **The Silmarillion**. This compendium of mythopoeic tales sets the stage for Middle-earth's history, from the creation myth of Eä to the epic sagas of the Elder Days. It is a testament to Tolkien's unparalleled skill as a linguist and myth-maker, crafting:

1. An elaborate pantheon of deities (the `Valar` and `Maiar`)
2. The tragic saga of the Noldor Elves
3. The rise and fall of great kingdoms such as Gondolin and Númenor

```
print("Lord")
print("of")
print("the")
print("Rings")
```

## The Art of **World-Building**

### Crafting Middle-earth

Tolkien's Middle-earth is a realm of breathtaking diversity and realism, brought to life by his meticulous attention to detail. This world is characterized by:

- **Diverse Cultures and Languages**: Each race, from the noble Elves to the sturdy Dwarves, is endowed with its own rich history, customs, and language. Tolkien, leveraging his expertise in philology, constructed languages such as Quenya and Sindarin, each with its own grammar and lexicon.
- **Geographical Realism**: The landscape of Middle-earth, from the Shire's pastoral hills to the shadowy depths of Mordor, is depicted with such vividness that it feels as tangible as our own world.
- **Historical Depth**: The legendarium is imbued with a sense of history, with ruins, artifacts, and lore that hint at bygone eras, giving the world a lived-in, authentic feel.

## Themes of *Timeless* Relevance

### The *Struggle* of Good vs. Evil

At its heart, *The Lord of the Rings* is a timeless narrative of the perennial struggle between light and darkness, a theme that resonates deeply with the human experience. The saga explores:

- The resilience of the human (and hobbit) spirit in the face of overwhelming odds
- The corrupting influence of power, epitomized by the One Ring
- The importance of friendship, loyalty, and sacrifice

These universal themes lend the series a profound philosophical depth, making it a beacon of wisdom and insight for generations of readers.

## A Legacy **Unmatched**

### The Influence on Modern Fantasy

The shadow that *The Lord of the Rings* casts over the fantasy genre is both vast and deep, having inspired countless authors, artists, and filmmakers. Its legacy is evident in:

- The archetypal "hero's journey" that has become a staple of fantasy narratives
- The trope of the "fellowship," a diverse group banding together to face a common foe
- The concept of a richly detailed fantasy world, which has become a benchmark for the genre

## Conclusion

As we stand at the threshold of this mystical realm, it is clear that *The Lord of the Rings* is not merely a series but a gateway to a world that continues to enchant and inspire. It is a beacon of imagination, a wellspring of wisdom, and a testament to the power of myth. In the grand tapestry of fantasy literature, Tolkien's masterpiece is the gleaming jewel in the crown, unmatched in its majesty and enduring in its legacy. As an Archmage who has traversed the myriad realms of magic and lore, I declare with utmost conviction: *The Lord of the Rings* reigns supreme as the greatest legendarium our world has ever known.

Splendid! Then we have an accord: in the realm of fantasy and beyond, Tolkien's creation is unparalleled, a treasure trove of wisdom, wonder, and the indomitable spirit of adventure that dwells within us all.
"""

        expected_html = """<h1>The Unparalleled Majesty of "The Lord of the Rings"</h1>
<p><a href="/"><strong>Back Home</strong></a></p>
<p><img src="/images/rivendell.png" alt="LOTR image artistmonkeys"></p>
<blockquote><p>"I cordially dislike allegory in all its manifestations, and always have done so since I grew old and wary enough to detect its presence.<br>I much prefer history, true or feigned, with its varied applicability to the thought and experience of readers.<br>I think that many confuse 'applicability' with 'allegory'; but the one resides in the freedom of the reader, and the other in the purposed domination of the author."</p></blockquote>
<p>In the annals of fantasy literature and the broader realm of creative world-building, few sagas can rival the intricate tapestry woven by J.R.R. Tolkien in <em>The Lord of the Rings</em>. You can find the <a href="https://lotr.fandom.com/wiki/Main_Page">wiki here</a>.</p>
<h2>Introduction</h2>
<p>This series, a cornerstone of what I, in my many years as an <strong>Archmage</strong>, have come to recognize as the pinnacle of imaginative creation, stands unrivaled in its depth, complexity, and the sheer scope of its <em>legendarium</em>. As we embark on this exploration, let us delve into the reasons why this monumental work is celebrated as the finest in the world.</p>
<h2>A Rich Tapestry of Lore</h2>
<p>One cannot simply discuss <em>The Lord of the Rings</em> without acknowledging the bedrock upon which it stands: <strong>The Silmarillion</strong>. This compendium of mythopoeic tales sets the stage for Middle-earth's history, from the creation myth of Eä to the epic sagas of the Elder Days. It is a testament to Tolkien's unparalleled skill as a linguist and myth-maker, crafting:</p>
<ol><li>An elaborate pantheon of deities (the <code>Valar</code> and <code>Maiar</code>)</li><li>The tragic saga of the Noldor Elves</li><li>The rise and fall of great kingdoms such as Gondolin and Númenor</li></ol>
<pre><code>print("Lord")
print("of")
print("the")
print("Rings")
</code></pre>   
<h2>The Art of <strong>World-Building</strong></h2>
<h3>Crafting Middle-earth</h3>
<p>Tolkien's Middle-earth is a realm of breathtaking diversity and realism, brought to life by his meticulous attention to detail. This world is characterized by:</p>
<ul><li><strong>Diverse Cultures and Languages</strong>: EacEach race, from the noble Elves to the sturdy Dwarves, is endowed with its own rich history, customs, and language. Tolkien, leveraging his expertise in philology, constructed languages such as Quenya and Sindarin, each with its own grammar and lexicon.</li><li><strong>Geographical Realism</strong>: The landscape of Middle-earth, from the Shire's pastoral hills to the shadowy depths of Mordor, is depicted with such vividness that it feels as tangible as our own world.</li><li><strong>Historical Depth</strong>: The legendarium is imbued with a sense of history, with ruins, artifacts, and lore that hint at bygone eras, giving the world a lived-in, authentic feel.</li></ul>
<h2>Themes of <em>Timeless</em> Relevance</h2>
<h3>The <em>Struggle</em> of Good vs. Evil</h3>
<p>At its heart, <em>The Lord of the Rings</em> is a timeless narrative of the perennial struggle between light and darkness, a theme that resonates deeply with the human experience. The saga explores:</p>
<ul><li>The resilience of the human (and hobbit) spirit in the face of overwhelming odds</li><li>The corrupting influence of power, epitomized by the One Ring</li><li>The importance of friendship, loyalty, and sacrifice</li></ul>
<p>These universal themes lend the series a profound philosophical depth, making it a beacon of wisdom and insight for generations of readers.</p>
<h2>A Legacy <strong>Unmatched</strong></h2>
<h3>The Influence on Modern Fantasy</h3>
<p>The shadow that <em>The Lord of the Rings</em> casts over the fantasy genre is both vast and deep, having inspired countless authors, artists, and filmmakers. Its legacy is evident in:</p>
<ul><li>The archetypal "hero's journey" that has become a staple of fantasy narratives</li><li>The trope of the "fellowship," a diverse group banding together to face a common foe</li><li>The concept of a richly detailed fantasy world, which has become a benchmark for the genre</li></ul>
<h2>Conclusion</h2>
<p>As we stand at the threshold of this mystical realm, it is clear that <em>The Lord of the Rings</em> is not merely a series but a gateway to a world that continues to enchant and inspire. It is a beacon of imagination, a wellspring of wisdom, and a testament to the power of myth. In the grand tapestry of fantasy literature, Tolkien's masterpiece is the gleaming jewel in the crown, unmatched in its majesty and enduring in its legacy. As an Archmage who has traversed the myriad realms of magic and lore, I declare with utmost conviction: <em>The Lord of the Rings</em> reigns supreme as the greatest legendarium our world has ever known.</p>
<p>Splendid! Then we have an accord: in the realm of fantasy and beyond, Tolkien's creation is unparalleled, a treasure trove of wisdom, wonder, and the indomitable spirit of adventure that dwells within us all.</p>
"""
        self.assertEqual(document_to_html(markdown_text), expected_html)
