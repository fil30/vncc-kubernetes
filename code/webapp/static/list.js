function get_elements(button_element) {

    const form_element = button_element.parentElement;
    const car_make = form_element['brand'].value;
    const year_min = form_element['yearMin'].value;
    const year_max = form_element['yearMax'].value;
    const price_min = form_element['priceMin'].value;
    const price_max = form_element['priceMax'].value;

    $('.list').empty()

    if (car_make && year_min && year_max && price_min && price_max) {
        $.get("http://localhost:5000/get_cars", {}, function (data) {
            if (data) {
                for (const car of data) {
                    if(car['car_make'] == car_make && car['prod_year'] >= year_min && car['prod_year'] <= year_max && car['price'] >= price_min && car['price'] <= price_max) {
                        $('.list').prepend(create_list(car))
                    }
                }
            }
        })
    }
}


function create_list(car) {
    const car_list = $('<li/>')
    car_list.append($('<span/>', { text: car['car_make'] + ', ' + car['car_model'] + ', ' + car['prod_year'] + ', ' + car['engine_size'] + ', ' + car['horsepower'] + ', ' + car['torque'] + ', ' + car['acceleration'] + ', ' + car['price']}))
    return car_list;
}