var scrollBounds = {}

titleArrowListener = () => {
    let languages = document.querySelector('#languages h2');
    scrollToTarget(languages);
}
languagesArrowListener = () => {
    let projects = document.querySelector('#projects h2');
    scrollToTarget(projects)
}

scrollToTarget = (target) => {
    let container = document.querySelector('#page_container');
    // let difference = target.getBoundingClientRect().top;
    target.scrollIntoView({behavior: "smooth"})
}



window.addEventListener('load', function () {
    document.querySelector('#title-container .down-arrow').addEventListener("click",titleArrowListener);
    document.querySelector('#languages-container .down-arrow').addEventListener("click",languagesArrowListener);
    
})



var scriptScrolling = false
window.addEventListener('scroll', function(e) {
    if( ! scriptScrolling ){

    }
})
