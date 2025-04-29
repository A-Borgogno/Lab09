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
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {nx.number_of_nodes(grafo_voli)}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di alberi: {nx.number_of_edges(grafo_voli)}"))
        for volo in grafo_voli.edges:
            self._view.txt_result.controls.append(ft.Text(volo))
        self._view.update_page()
