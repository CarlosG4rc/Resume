function loadInternalHeader(title) {
    const headerHTML = `
    <header class="bg-dark text-white py-4 mb-4 shadow">
        <div class="contenedor">
            <div class="d-flex justify-content-between align-items-center">
                <a href="index.html" class="text-decoration-none">
                    <h1 class="m-0 text-white" style="font-size: 2.5rem;">Carlos <span>García</span></h1>
                </a>
                <div class="text-end d-none d-md-block">
                    <p class="m-0 text-white-50"><small><label id='today'></label></small></p>
                </div>
            </div>
        </div>
        ${title ? `<div class="contenedor mt-3 border-top border-secondary pt-3"><h3 class="text-white m-0">${title}</h3></div>` : ''}
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