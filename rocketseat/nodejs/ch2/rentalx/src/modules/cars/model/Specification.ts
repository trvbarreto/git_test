import { v4 as uuidV4 } from "uuid";

class Specification {
    id?: string;
    name: string;
    description: string;
    created_at: Date;

    /**
     * esse construtor verificar se já tem ID criado para a categoria
     *  e cria se não houver
     */
    constructor() {
        if (!this.id) {
            this.id = uuidV4();
        }
    }
}

export { Specification };
