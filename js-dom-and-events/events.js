// btn1 - forma padrão de adicionar um evento
const btn1 = document.querySelector('#btn1');
btn1.addEventListener('click', () => {
    alert('Hello World');
});

// btn2 - usa named function como parâmetro
const btn2 = document.querySelector('#btn2');
btn2.addEventListener('click', alertFunction);

function alertFunction() {
    alert('YAY! YOU CLICKED ME');
};

// btn3 - acessa o objeto do evento
const btn3 = document.querySelector('#btn3');
btn3.addEventListener('click', function(e) {
    console.log(e);
    console.log(e.target);
    e.target.style.background = 'blue';
});


// buttons é uma nodelist com todos os elementos button
const buttons = document.querySelectorAll('button');

// .forEach itera sobre todos os botões
buttons.forEach((button) => {

    // adiciona um evento do tipo 'click' para cada um
    button.addEventListener('click', () => {
        alert(button.id);
    });
});