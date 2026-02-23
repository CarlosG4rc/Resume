function loadInternalHeader(title) {
    const headerHTML = `
    <header style="background-color: black;">
        <div class="contenedor">
            <div class="barra">
                <a href="index.html">
                    <h1 class="no-margin text-white">Carlos <span>García</span></h1>
                </a>
            </div>
            <b><p><u><label id='today'></label></u></p></b>
        </div>
        ${title ? `<div class="contenedor"><h3 class="text-white">${title}</h3></div>` : ''}
    </header>
    `;
    
    // Inserta el header al principio del body
    document.body.insertAdjacentHTML('afterbegin', headerHTML);

    // Lógica de la fecha
    const dateOptions = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    const today = new Date().toLocaleDateString('en-US', dateOptions);
    const todayLabel = document.getElementById('today');
    if (todayLabel) todayLabel.textContent = today;
}