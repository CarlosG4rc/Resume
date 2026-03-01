function loadHeadDependencies(includePyScript = false) {
    const dependencies = [
        // Bootstrap 5 CSS
        '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">',
        // Bootstrap 5 JS Bundle
        '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>',
        // jQuery
        '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>',
        // FontAwesome
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css" integrity="sha512-z3gLpd7yknf1YoNbCzqRKc4qyor8gaKU1qmn+CShxbuBusANI9QpRohGBreCFkKxLhei6S9CQXFEbbKuqLg0DA==" crossorigin="anonymous" referrerpolicy="no-referrer" />',
        // Google Fonts
        '<link href="https://fonts.googleapis.com/css2?family=Open+Sans&family=Roboto:wght@400;700&display=swap" rel="stylesheet">',
        "<link href='https://fonts.googleapis.com/css?family=Orbitron' rel='stylesheet' type='text/css'>",
        // Local CSS
        '<link rel="stylesheet" href="css/normalize.css">',
        '<link rel="stylesheet" href="css/main.css">'
    ];

    if (includePyScript) {
        dependencies.push('<link rel="stylesheet" href="https://pyscript.net/releases/2025.11.1/core.css">');
        dependencies.push('<script type="module" src="https://pyscript.net/releases/2025.11.1/core.js"></script>');
    }

    document.head.insertAdjacentHTML('beforeend', dependencies.join('\n'));
}