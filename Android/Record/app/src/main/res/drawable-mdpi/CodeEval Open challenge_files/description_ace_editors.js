var set_description_editor = function(editor_el){
    var desc_editor = ace.edit(editor_el);
    desc_editor.setTheme("ace/theme/github");
    desc_editor.getSession().setMode("ace/mode/text");
    desc_editor.setReadOnly(true);
    desc_editor.session.setUseWrapMode(true);
    desc_editor.setHighlightActiveLine(false);
    return desc_editor
};

var heightUpdateFunction = function(editor, editor_el) {
    // http://stackoverflow.com/questions/11584061/
    var newHeight =
              editor.getSession().getScreenLength()
              * editor.renderer.lineHeight
              + editor.renderer.scrollBar.getWidth();

    $(editor_el).height(newHeight.toString() + "px");
    //$('#editor-section').height(newHeight.toString() + "px");

    // This call is required for the editor to fix all of
    // its inner structure for adapting to a change in size
    editor.resize();
};

var challenge_description_input_output_editors = function(elements, dynamic_height){
    if (typeof elements === 'undefined'){
        elements = $('.description-input-output');
    }
    if (typeof dynamic_height === 'undefined'){
        dynamic_height = true;
    }
    $.each(elements, function( index, editor_el ) {
        var editor = set_description_editor(editor_el);
        if (dynamic_height){
            heightUpdateFunction(editor, editor_el);
        }
    });
};

//$(document).ready(function(){
//    challenge_description_input_output_editors();
//});