window.addEventListener("DOMContentLoaded", () =>{
    //only handle one particular tablist; if you have multiple tabs
    //Lists might  even be nested, you have to apply this code for each one.
    const tabList = document.querySelector('[role="tablist"]');
    const tabs = tabList.querySelectorAll(':scope > [role="tab"]');

    //Add a click event handler to each tab
    tabs.forEach((tab)=>{
        tab.addEventListener("click", changeTabs);
    });

    //Enable arrow navigation between tabs in the tablist
    let tabFocus = 0;

    tabList.addEventListener("keydown", (e) =>{
        //Move right
        if (e.key === "ArrowRight" || e.key === "ArrowLeft"){
            tabs[tabFocus].setAttribute('tabindex', -1);

            if(e.key === "ArrowRight"){
                tabFocus ++;
                //if we are at the end move to the start
                if(tabFocus >= tabs.length){
                    tabFocus = 0;
                }
            }
            //move to the left
            else if(e.key ==="ArrowLeft"){
                tabFocus --;
                //if we are at the start move to the end
                if(tabFocus < 0){
                    tabFocus = tabs.length - 1;
                }
            }
            tabs[tabFocus].setAttribute("tabIndex", 0)
            tabs[tabFocus].focus();
        }
    });

    //Add a click event listener for caret expansion
    const caretContainer = document.getElementsByClassName("caret-container")[0];

    const carets = caretContainer.querySelectorAll('[class="caret-expander"]');

    

    carets.forEach((caret) => {
         caret.addEventListener("click", expandCaret);
    });
});

function changeTabs(e){
    const targetTab = e.target;
    const tabList = targetTab.parentNode;
    const tabGroup = document.querySelector(".tab-panel-container");//this is where it went wrong.  my panels are in a different container
   
    //Remove all current selected tabs
    tabList.querySelectorAll(':scope > [aria-selected = "true"]').forEach((t)=>{t.setAttribute("aria-selected", false)});

    //put all div indicators in hiddeon mode
    tabList.querySelectorAll('[class="star-tabs-slider"]').forEach((s) => {s.setAttribute("hidden",true)});

    //set this tab as selected
    targetTab.setAttribute("aria-selected", true);
    targetTab.querySelector('[class="star-tabs-slider"]').removeAttribute("hidden");

    //Hide all tab panels
    tabGroup.querySelectorAll(':scope > [role="tabpanel"]').forEach((p) => {p.setAttribute("hidden", true)});
    //Show the selected tab
    console.log(`${targetTab.getAttribute("aria-controls")}`);
    tabGroup.querySelector(`#${targetTab.getAttribute("aria-controls")}`).removeAttribute("hidden");
}


function expandCaret(e){
    const targetCaret = e.target;
    const caretContainer = document.querySelector(".caret-container");

    console.log(caretContainer);
    
    //create a nodeList containing elements with the role = caret
    const expandedCaret = caretContainer.querySelectorAll('[class="caret-expanded"]');
    

    [...expandedCaret].forEach((p) => {
        p.setAttribute("hidden",true)
    });
    
    
    console.log(`${targetCaret.getAttribute("aria-controls")}`);
    //show the selected caret
    caretContainer.querySelector(`#${targetCaret.getAttribute("aria-controls")}`).removeAttribute("hidden");

}

