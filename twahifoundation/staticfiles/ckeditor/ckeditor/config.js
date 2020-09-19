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
};

CKEDITOR.plugins.addExternal("youtube", "../plugins/youtube/");

config.extraPlugins = "youtube";
