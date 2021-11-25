
/*

It's necessary to communicate the iframe with the Rocketbot view

*/

var message = {
    type: 'iframe',
    commands: {}
}
var SendMessage = function () {
    parent.postMessage(message, "*");
}
$('#firstColor').on('change', function (e) {
    // e.data.printer
    message.commands['firstColor'] = $(this).val();
    SendMessage();
})

// $('#secondColor').on('change', function (e) {
//     // e.data.printer
//     message.commands['secondColor'] = $(this).val();
//     SendMessage();
// })

var eventMethod = window.addEventListener ? "addEventListener" : "attachEvent";
var eventer = window[eventMethod];
var messageEvent = eventMethod == "attachEvent" ? "onmessage" : "message";

// Listen to message from child window || Esto es cuando haces doble click en la ventana de R B
eventer(messageEvent, function (e) {
    console.log('parent received message!:  ', e.data);

    if (e.data && e.data.firstColor) {
        $("#firstColor").val(e.data.firstColor)
    }

    // if (e.data && e.data.secondColor) {
    //     $("#secondColor").val(e.data.secondColor)
    // }
    // Ver como hacer para q quede el color up ?
});

function getDataFromRB({module_name, command_name}) {
    let api = document.URL.split("module")[0]
    var formData = new FormData()
    let command_ = {
        "project": {
            "profile": {
                "name": module_name,
                "description": "",
                "version": "2020.12.30"
            },
            "vars": [
                {
                    "name": module_name + "_fake_var",
                    "data": "",
                    "type": "string",
                    "collapse": true,
                    "$$hashKey": "object:1204"
                }
            ],
            "commands": [
                {
                    "father": "module",
                    "command": `{\"module_name\":\"${module_name}\",\"module\":\"${command_name}\",\"var_name\":\"${module_name + "_fake_var"}\"}`,
                    "option": "",
                    "var": "",
                    "index": 0,
                    "group": "scripts",
                    "execute": 0,
                    "if": "",
                    "children": [],
                    "else": [],
                    "id": "50ad1403-a6d8-d1da-c654-77eba1a4830a",
                    "mode_live": true,
                    "getvar": "",
                    "extra_data": null,
                    "screenshot": "",
                    "execute_debbug": 0,
                    "img": ""
                }
            ],
            "ifs": []
        }
    }

    formData.append('info', JSON.stringify(command_))
    formData.append('db', "")
    var data = null
    return fetch(api + "execute", {
        method: "POST",
        body: formData,
    }).then(res => res.json())
        .catch(error => console.error('Error:', error))
        .then(response => {
            data = response.vars[0].data
            console.log("aca viene la data")
            console.log(typeof data)
            return eval( data )
        });
}