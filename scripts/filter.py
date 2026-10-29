import sys
import xml.etree.ElementTree as ET

strs = ['[AI]']

def filter_items(parent, items, title_tag, is_filter_in):
  for item in items:
    title = item.findtext(title_tag) or ""
    for str in strs:
      contains_str = str.casefold() in title.casefold()
      if (is_filter_in and not contains_str) or (not is_filter_in and contains_str):
        parent.remove(item)

def filter(is_filter_in):
  global strs
  tree = ET.parse(sys.stdin.buffer)
  root = tree.getroot()

  if root.tag == "rss":
    for channel in root.iter("channel"):
      filter_items(channel, list(channel.findall("item")), "title", is_filter_in)
  elif root.tag == "{http://purl.org/atom/ns#}feed":
    ET.register_namespace("", "http://purl.org/atom/ns#")
    filter_items(root, list(root.findall("{http://purl.org/atom/ns#}entry")), "{http://purl.org/atom/ns#}title", is_filter_in)
  else:
    raise Exception("Unexpected root: " + root.tag)


  tree.write(
    sys.stdout.buffer,
    encoding="utf-8",
    xml_declaration=True
  )
