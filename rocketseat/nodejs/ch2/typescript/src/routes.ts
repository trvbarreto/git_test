import {Request, response, Response} from 'express';
import CreateCourseService from './CreateCourseService';

export function createCourse(req: Request, res: Response) {
    CreateCourseService.execute({
        name: "NodeJS",
        educator: "Dani",
    });

    CreateCourseService.execute({
        name: "ReactJS",
        educator: "Diego",
        duration: 4,
    });

    return res.send();
}