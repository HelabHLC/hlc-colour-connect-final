
document.addEventListener('DOMContentLoaded', () => {
    const deltaSlider = document.getElementById('deltaSlider');
    const deltaVal = document.getElementById('deltaVal');
    const extractBtn = document.getElementById('extractBtn');
    const imageUpload = document.getElementById('imageUpload');
    const grid = document.getElementById('colorGrid');

    const infoName = document.getElementById('infoName');
    const infoHex = document.getElementById('infoHex');
    const infoLab = document.getElementById('infoLab');
    const preview = document.getElementById('colorPreview');

    deltaSlider.addEventListener('input', () => {
        deltaVal.textContent = deltaSlider.value;
    });

    extractBtn.addEventListener('click', () => {
        const file = imageUpload.files[0];
        if (!file) return alert("Bitte ein Bild hochladen.");

        const img = new Image();
        const reader = new FileReader();
        reader.onload = e => img.src = e.target.result;
        reader.readAsDataURL(file);

        img.onload = () => {
            const canvas = document.getElementById('hiddenCanvas');
            const ctx = canvas.getContext('2d');
            canvas.width = img.width;
            canvas.height = img.height;
            ctx.drawImage(img, 0, 0);

            const data = ctx.getImageData(0, 0, img.width, img.height).data;
            const colors = {};
            for (let i = 0; i < data.length; i += 4) {
                const r = data[i], g = data[i+1], b = data[i+2];
                const hex = '#' + [r,g,b].map(x => x.toString(16).padStart(2,'0')).join('');
                colors[hex] = (colors[hex] || 0) + 1;
            }

            const topColors = Object.entries(colors)
                .sort((a,b) => b[1]-a[1])
                .slice(0, 5)
                .map(entry => entry[0]);

            fetch(`/api/match?colors=${topColors.join(',')}&delta=${deltaSlider.value}`)
                .then(res => res.json())
                .then(matches => {
                    grid.innerHTML = '';
                    matches.forEach(c => {
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

                        grid.appendChild(div);
                    });
                });
        };
    });
});
