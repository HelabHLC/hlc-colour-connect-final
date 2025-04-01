
let palette = [];

document.addEventListener('DOMContentLoaded', () => {
    const select = document.getElementById('iccSelect');
    const grid = document.getElementById('colorGrid');
    const exportBtn = document.getElementById('exportBtn');

    const infoName = document.getElementById('infoName');
    const infoHex = document.getElementById('infoHex');
    const infoLab = document.getElementById('infoLab');
    const preview = document.getElementById('colorPreview');

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
                palette = [];
                colors.forEach(c => {
                    const div = document.createElement('div');
                    div.className = 'colorBox';
                    div.style.background = c.hex;
                    div.title = c.name;

                    div.addEventListener('mouseenter', () => {
                        infoName.textContent = c.name;
                        infoHex.textContent = c.hex;
                        infoLab.textContent = c.lab.join(', ');
                        preview.style.background = c.hex;
                    });

                    div.addEventListener('click', () => {
                        palette.push(c);
                    });

                    grid.appendChild(div);
                });
            });
    });

    exportBtn.addEventListener('click', () => {
        const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(palette, null, 2));
        const dl = document.createElement('a');
        dl.setAttribute("href", dataStr);
        dl.setAttribute("download", "palette.json");
        dl.click();
    });
});
