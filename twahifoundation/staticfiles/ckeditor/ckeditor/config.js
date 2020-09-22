CKEDITOR.editorConfig = function (config) {
  config.toolbarGroups = [
    { name: "document", groups: ["mode", "document", "doctools"] },
    { name: "clipboard", groups: ["clipboard", "undo"] },
    { name: "styles", groups: ["styles"] },
    { name: "basicstyles", groups: ["basicstyles", "cleanup"] },
    { name: "colors", groups: ["colors"] },
    {
      name: "editing",
      groups: ["find", "selection", "spellchecker", "editing"],
    },
    { name: "forms", groups: ["forms"] },
    {
      name: "paragraph",
      groups: ["indent", "blocks", "align", "list", "bidi", "paragraph"],
    },
    { name: "links", groups: ["links"] },
    { name: "insert", groups: ["insert"] },
    { name: "tools", groups: ["tools"] },
    { name: "others", groups: ["others"] },
    { name: "about", groups: ["about"] },
  ];

  config.removeButtons =
    "Save,NewPage,Print,Cut,Copy,Paste,PasteText,PasteFromWord,Form,Checkbox,Radio,TextField,Textarea,Select,Button,ImageButton,HiddenField,Flash,About";

  config.extraPlugins = "youtube,autolink";
};

// Define changes to default configuration here. For example:
// config.language = 'fr';
// config.uiColor = '#AADC6E';
CKEDITOR.on("instanceReady", function (ev) {
  var writer = ev.editor.dataProcessor.writer;
  // The character sequence to use for every indentation step.
  writer.indentationChars = "  ";

  var dtd = CKEDITOR.dtd;
  // Elements taken as an example are: block-level elements (div or p), list items (li, dd), and table elements (td, tbody).
  for (var e in CKEDITOR.tools.extend(
    {},
    dtd.$block,
    dtd.$listItem,
    dtd.$tableContent
  )) {
    ev.editor.dataProcessor.writer.setRules(e, {
      // Indicates that an element creates indentation on line breaks that it contains.
      indent: false,
      // Inserts a line break before a tag.
      breakBeforeOpen: false,
      // Inserts a line break after a tag.
      breakAfterOpen: false,
      // Inserts a line break before the closing tag.
      breakBeforeClose: false,
      // Inserts a line break after the closing tag.
      breakAfterClose: false,
    });
  }

  for (var e in CKEDITOR.tools.extend(
    {},
    dtd.$list,
    dtd.$listItem,
    dtd.$tableContent
  )) {
    ev.editor.dataProcessor.writer.setRules(e, {
      indent: true,
    });
  }

  ev.editor.dataProcessor.htmlFilter.addRules({
    elements: {
      img: function (el) {
        // Add bootstrap "img-responsive" class to each inserted image
        el.addClass("img-responsive");

        // Remove inline "height" and "width" styles and
        // replace them with their attribute counterparts.
        // This ensures that the 'img-responsive' class works
        var style = el.attributes.style;

        if (style) {
          // Get the width from the style.
          var match = /(?:^|\s)width\s*:\s*(\d+)px/i.exec(style),
            width = match && match[1];

          // Get the height from the style.
          match = /(?:^|\s)height\s*:\s*(\d+)px/i.exec(style);
          var height = match && match[1];

          // Replace the width
          if (width) {
            el.attributes.style = el.attributes.style.replace(
              /(?:^|\s)width\s*:\s*(\d+)px;?/i,
              ""
            );
            el.attributes.width = width;
          }

          // Replace the height
          if (height) {
            el.attributes.style = el.attributes.style.replace(
              /(?:^|\s)height\s*:\s*(\d+)px;?/i,
              ""
            );
            el.attributes.height = height;
          }
        }

        // Remove the style tag if it is empty
        if (!el.attributes.style) delete el.attributes.style;
      },
    },
  });
});
