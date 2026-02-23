const footerHTML = `
<footer class="site-footer">
    <div class="contenedor">
        <div class="barra">
            <a href="index.html" style="text-decoration:none;">
                <p class="no-margin">Carlos <span>García</span></p>
            </a>
            <nav class="navegacion-foot" id="myNavbar">
                <a href="index.html#sobremi">About me |</a>
                <a href="index.html#proyectos"> Projects | </a>
                <a href="index.html#contacto">Contact me</a>
            </nav>
            <nav>
                <a href="file/CV_.pdf" class="btn btn-secudnario" target="_blank">Download CV</a>
            </nav>
        </div>
    </div>
</footer>
`;
document.body.insertAdjacentHTML('beforeend', footerHTML);