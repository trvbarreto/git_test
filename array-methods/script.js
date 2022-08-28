let humanBuildings = ["Town Hall", "Barracks", "Farm", "Lumber Mill"];

// toString() transforma o array em uma string, valores separado por virgula
let toString = humanBuildings.toString();

console.log(toString); // Town Hall,Barracks,Farm,Lumber Mill 

// join() funciona como o toString porém é possível indicar um separador
let joined = humanBuildings.join(" | ");

console.log(joined); // Town Hall | Barracks | Farm | Lumber Mill

// pop() remove o último elemento e retorna ele
let popped = humanBuildings.pop();
console.log(popped); // Lumber Mill
console.log(humanBuildings); // (3) ['Town Hall', 'Barracks', 'Farm']

// push() adiciona o elemento na última posição e retorna o novo tamanho do array
let pushed = humanBuildings.push("Lumber Mill");
console.log(pushed); // 4
console.log(humanBuildings); // ['Town Hall', 'Barracks', 'Farm', 'Lumber Mill']

// shift() remove o primeiro elemento e move todos os outros pra um indice a menos, e retorna o elemento que foi removido
let shifted = humanBuildings.shift();
console.log(shifted); // Town Hall
console.log(humanBuildings); // (3) ['Barracks', 'Farm', 'Lumber Mill']

// unshift() adiciona o elemento na primeira posição, e retorna o novo tamanho do array
let unshifted = humanBuildings.unshift("Town Hall");
console.log(unshifted); // 4
console.log(humanBuildings); // (4) ['Town Hall', 'Barracks', 'Farm', 'Lumber Mill']