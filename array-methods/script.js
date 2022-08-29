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

// length mostra o tamanho do array
console.log(humanBuildings.length); // 4

// delete apaga o elemento, mas deixa 'undefined' no indice
delete humanBuildings[0];
console.log(humanBuildings); // (4) [vazio, 'Barracks', 'Farm', 'Lumber Mill']

// concat cria um novo array juntando arrays existentes, não muda os arrays existentes, pode ser passado mais de um array como argumento ou valores
const orcBuildings = ["Bestiary", "Orc Burrow", "War Mill"];
const orcAndHumanBuildings = humanBuildings.concat(orcBuildings);

console.log(orcAndHumanBuildings); // (7) [vazio, 'Barracks', 'Farm', 'Lumber Mill', 'Bestiary', 'Orc Burrow', 'War Mill']

// splice() adiciona novos items ao array em uma posição especifica e indica se quer remover elementos, retorna os elementos removidos
let spliced = humanBuildings.splice(0, 1);
humanBuildings.splice(0, 0, "Town Hall");

console.log(spliced); // [vazio]
console.log(humanBuildings); // (4) ['Town Hall', 'Barracks', 'Farm', 'Lumber Mill']
