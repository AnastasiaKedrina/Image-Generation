
        let ad_div = document.getElementById("ad_div");

        
        var style_obj = new Object();
        style_obj.font_size = window.getComputedStyle(ad_div).fontSize;
        style_obj.background_color  = window.getComputedStyle(ad_div).backgroundColor;

        function changeSizeBySlider() {
            let slider = document.getElementById("slider");
            ad_div.style.fontSize = slider.value + "px";
            document.getElementById("font-size-text").textContent = "Размер текста: " + slider.value + "px";
            style_obj.font_size = slider.value + "px";
        }


        var options = document.getElementsByName('option');
        var option_value;
        for(var i = 0; options.length; i++){
            if(options[i].checked){
                option_value = options[i].value;
                break;
            }
        }
        const background_colors = ['white', 'lavender', 'moccasin', 'pink', 'lightcyan'];
    
        const radio_container = document.querySelector("#radio_container");
        radio_container.innerHTML = background_colors.map((color) => `<div>
                <input type="radio" name="color" value="${color}" id="${color}">
                 <label for="${color}">${color}</label>
            </div>`).join(' ');
        
        // add an event listener for the change event
        const radioButtons = document.querySelectorAll('input[name="color"]');
        for(const radioButton of radioButtons){
            radioButton.addEventListener('change', showSelected);
        }        
        
        function showSelected(e) {
            if (this.checked) {
                document.querySelector('#radio-check-text').innerText = `Цвет фона: ${this.value}`;
                ad_div.style.backgroundColor = this.value
                style_obj.background_color  = this.value;
            }
        }


        function save_changes() {
            console.log(style_obj)
            // var jsonString= JSON.stringify(style_obj);
            filename = 'style_changes'
            save_json_file(style_obj, filename);
        }

        const save_json_file = (obj, filename) => {
            const blob = new Blob([JSON.stringify(obj, null, 2)], {
                type: 'application/json',
            });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `${filename}.json`;
            a.click();
            URL.revokeObjectURL(url);
        };

        