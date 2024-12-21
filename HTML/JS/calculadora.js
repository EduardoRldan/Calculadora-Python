let display = document.getElementById('display');
let expression = '';

function appendNumber(number) {
    expression += number;
    display.innerText = expression;
}

function appendOperator(operator) {
    if (expression && !isOperator(expression.slice(-1))){
        expression += operator;
        display.innerText = expression;
    }
}

function appendDot() {
    if (!expression.includes('.') || expression.match(/(\d+\.\d*[^0-9]*)$/)) {
        expression += '.';
        display.innerText = expression;
    }
}

function clearDisplay(){
    expression = '';
    display.innerText = '';
}



function calculate() {
    try {
        expression = eval(expression).toString();
        display.innerText = expression;
    } catch (e) {
        display.innerText = 'Error';
        expression = '';
    }
}

function isOperator(char) {
    return ['+', '-', '*', '/'].includes(char);
}