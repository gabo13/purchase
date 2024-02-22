function validate() {
    const shop = document.querySelector('#shop');
    const cost = document.querySelector('#cost');
    
    alert("Validate error");
    return false;
}

function setMonthRangeInput() {
    const monthInput = document.querySelector('#month');
    const lastDay = new Date(2024,Number(monthInput.value),0).getDate();
    const dayInput = document.querySelector('#day');
    let htmlTemplate = '';    
    for (let i=1; i++; i<= lastDay) {
        htmlTemplate +=`<option value=${i}>${i}</option>`;
    }
    dayInput.innerHTML = htmlTemplate;
}

document.queeySelector('#month').addEventListener('change',()=>{
    setMonthRangeInput();
})
