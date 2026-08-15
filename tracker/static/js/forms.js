console.log('forms.js')
function saveOnChange(element){
    console.log('BANANA', element)
    let parent = element.parentElement;
    console.log(parent)
    while (
        parent !== document.body 
        && parent.tagName.toLowerCase() !== 'form'
    ){
        parent = parent.parentElement;
        console.log(parent)
    }

    if (parent !== document.body) {
        parent.submit();
    }
}