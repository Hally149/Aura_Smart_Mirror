/* frontend */

function askAura() {
    fetch('/api/music?mood=happy')
        .then(response => response.json())
        .then(data => {
            let audio = document.getElementById('auraResponse');
            audio.src = data.preview_url;
            audio.play();
        });
}


/* 
 * Copyright © 2026 Osasere H. Ero. All rights reserved.
 * Proprietary and confidential. Unauthorized copying of this file, via any medium, is strictly prohibited.
 */
