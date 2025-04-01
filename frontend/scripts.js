
document.addEventListener('DOMContentLoaded', () => {
    const select = document.getElementById('iccSelect');
    const grid = document.getElementById('colorGrid');

    fetch('/api/icc-profiles')
        .then(res => res.json())
        .then(data => {
            data.forEach(profile => {
                const opt = document.createElement('option');
                opt.value = profile;
                opt.textContent = profile;
                select.appendChild(opt);
            });
        });

    select.addEventListener('change', () => {
        const icc = select.value;
        fetch(`/api/colors?icc=${icc}`)
            .then(res => res.json())
            .then(colors => {
                grid.innerHTML = '';
                colors.forEach(c => {
                    const div = document.createElement('div');
                    div.style.background = c.hex;
                    div.style.width = '50px';
                    div.style.height = '50px';
                    div.title = c.name;
                    grid.appendChild(div);
                });
            });
    });
});
