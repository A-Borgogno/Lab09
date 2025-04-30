import flet as ft
import networkx as nx


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza(self, e):
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Caricamento in corso",size=22, weight=ft.FontWeight.BOLD))
        self._view.update_page()
        grafo_voli = self._model.analizza(self._view.distanza.value)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {nx.number_of_nodes(grafo_voli)}", size=16, italic=True))
        self._view.txt_result.controls.append(ft.Text(f"Numero di alberi: {nx.number_of_edges(grafo_voli)}", size=16, italic=True))
        for volo in grafo_voli.edges(data=True):
            self._view.txt_result.controls.append(ft.Text(f"{volo[0]} --> {volo[1]}, {volo[2]["weight"]} miglia", size=16))
        self._view.update_page()
