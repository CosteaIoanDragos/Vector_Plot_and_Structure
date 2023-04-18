from infrastructure.VectorRepository import VectorRepoistory
from domain.MyVector import MyVector
from application.controller import VectorController
from ui.console import run
if __name__ == "__main__":
    controller = VectorController()
    run(controller)
