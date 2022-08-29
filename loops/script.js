const undeads = ["Acolyte", "Abomination", "Ghoul", "Banshee"]

// for...of ferramenta para percorrer uma coleção e executar algo
for (const unit of undeads) {
    console.log(unit); // o valor de cada elemento
}

// map() percorre cada elemento da coleção, executa algo e retorna uma nova coleção
function toUpper(string) {
    return string.toUpperCase();
}

const upperUndeads = undeads.map(toUpper);
console.log(upperUndeads); // (4) ['ACOLYTE', 'ABOMINATION', 'GHOUL', 'BANSHEE']
