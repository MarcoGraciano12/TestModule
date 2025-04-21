from db.session import init_db, SessionLocal
from domain.question import Question
from domain.exam import Exam
from domain.exam_manager import ExamManager


def run():
    init_db()
    session = SessionLocal()

    try:
        manager = ExamManager(session)

        exam = Exam("GF")
        exam.add_question(Question("¿En qué año se fundó Grupo Fórmula?", "En 1968"))
        exam.add_question(Question("¿Quién fundó Grupo Fórmula?", "Rogerio Azcárraga Madero"))
        exam.add_question(Question("¿Quién fundó Discos Orfeón?", "Rogerio Azcárraga Madero"))
        exam.add_question(Question("¿Cuándo se presentó oficialmente NAT?", "En marzo del 2023"))
        exam.add_question(Question("¿Qué significa NAT?", "Neural Artificial Technology"))
        exam.add_question(Question("¿Cuál es el nombre completo de NAT?", "Natalia"))
        exam.add_question(Question("¿Quién es NAT?", "Presentadora de Noticias creada con Inteligencia Artificial Generativa propiedad de Grupo Formula"))
        exam.add_question(Question("¿Quienes son los socios de Grupo Fórmula?", "Andrea Azcarraga Romandia, Lorenza Azcarraga Romandia y Jaime Azcárraga Romandía"))
        exam.add_question(Question("¿Quién es el Presidente del consejo de administración?", "Jaime Azcárraga Romandía"))
        exam.add_question(Question("¿Quién es el director de NextAI Solutions?", "Héctor Aguilar Cuevas"))
        exam.add_question(Question("¿En qué año se fundó TeleFórmula?", "1994"))
        exam.add_question(Question("¿Qué es PM Onstreet?", "PM Onstreet es una empresa comprometida con la venta de OOH (Out-Of-Home) en mobiliario urbano."))
        exam.add_question(Question("¿En qué año PM Onstreet fue condecorada con el Premio de Creatividad Publicitaria?", "2021"))
        exam.add_question(Question("¿Quién es Joaquín López-Dóriga?", "Periodista y conductor en Grupo Fórmula."))


        manager.create_exam(exam)
        print("Exam created successfully.")

        exams = manager.list_exams()
        for ex in exams:
            print(f"Exam ID: {ex.id}, Title: {ex.title}, Questions: {len(ex.questions)}")
            for q in ex.questions:
                print(f"  - Q{q.id}: {q.prompt} → {q.answer}")

    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        session.close()


if __name__ == "__main__":
    run()
