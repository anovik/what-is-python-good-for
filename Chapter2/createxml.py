import xml.etree.cElementTree as ET

root = ET.Element("root")
ET.SubElement(root, "introduction")
book = ET.SubElement(root, "book")

ET.SubElement(book, "chapter1", name="Python For Beginners", pagesnumber="100").text = "Would you like to learn some Python?"
ET.SubElement(book, "chapter2", name="Advanced Python", pagesnumber="300").text = "Let's go deeper!"
ET.SubElement(book, "chapter3", name="More Advanced Python", pagesnumber="1000").text = "Now you can write your own version of GPT-10."

tree = ET.ElementTree(root)

ET.indent(tree, space="\t", level=0)

tree.write("output.xml", encoding="utf-8")
