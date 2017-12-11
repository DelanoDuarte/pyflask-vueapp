export class Service {

    getNames = function () {
        let jsonData;
        fetch('http://127.0.0.1:5000/py-vue/api/test')
            .then(res => {
                res.json()
                    .then(res => {
                        jsonData = res
                    })
            })

        return jsonData;
    }

}