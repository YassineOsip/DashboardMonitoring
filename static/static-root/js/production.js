$(document).ready(function (){
    function httpClient(url, reqType, dataType, onSuccessFunction, data = {}) {
        $.ajax({
            url: url,
            type: reqType,
            dataType: dataType,
            success: onSuccessFunction,
            data: data
        });
    }
    let getUrl = window.location;
    let baseUrl = getUrl.protocol + "//" + getUrl.host + getUrl.pathname.split('/')[0];

    let intervalId = window.setInterval(function(){
        httpClient(baseUrl+productivityPerHoursDataUrl,'GET','json',(result,status)=>{
            for(let i=0;i<result.productivityPerHourYieldColorsData.length;i++){
                $(`#smallBox${i}`).addClass(result.productivityPerHourYieldColorsData[i].name);
                $(`.yield${i}`).empty();
                $(`.yield${i}`).append(`${result.productivityPerHourYieldData[i].val}<sup style="font-size: 20px">%</sup>`);
                $(`.chainHour${i}`).empty();
                $(`.chainHour${i}`).append(`<strong>${result.chainsData[i].fields.name}</strong>---<cite>${result.productivityPerHoursData[i].fields.hour}h</cite>`);
            }
        })
    }, 1000);

    // to stop the loop
    // clearInterval(intervalId)

});