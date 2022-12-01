
/**
 * name -string
 * duration - number
 * educator - string
 */

interface Course {
    name: string;
    duration?: number; // atributo opcional
    educator:string;
}

class CreateCourseService {
    // duration com o valor padrão de 8, caso não for informado
    execute({duration = 8, educator, name}: Course) {
        console.log(name, duration, educator);        
    };
};

export default new CreateCourseService();