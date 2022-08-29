const undeads = ["Acolyte", "Abomination", "Ghoul", "Banshee"]

// for...of ferramenta para percorrer uma coleção e executar algo
for (const unit of undeads) {
    console.log(unit); // o valor de cada elemento
}

// map() percorre cada elemento da coleção, executa algo e retorna uma nova coleção
function toUpper(string) {
    return string.toUpperCase();
}

const mapped = undeads.map(toUpper);
console.log(mapped); // (4) ['ACOLYTE', 'ABOMINATION', 'GHOUL', 'BANSHEE']

// filter() testa os items do array e os que passarem no teste são inseridos no novo array
function startWithA(string) {
    return string.startsWith('A');
}

const filtered = undeads.filter(startWithA);

console.log(filtered); // (2) ['Acolyte', 'Abomination']