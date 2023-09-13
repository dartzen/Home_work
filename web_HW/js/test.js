function showName(name='незнакомец'){
alert(`Спасибо, что представился ${name}`);
}

let test = prompt("Как тебя зовут?", "Введите имя");
if (test == '')
showName();
else
showName(test);
