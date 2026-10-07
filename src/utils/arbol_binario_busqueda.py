class _Nodo:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None
        self._cantidad = 0

    def __len__(self):
        return self._cantidad

    def insertar(self, clave, valor):
        if self.raiz is None:
            self.raiz = _Nodo(clave, valor)
            self._cantidad = 1
            return True
        nodo = self.raiz
        while True:
            if clave == nodo.clave:
                nodo.valor = valor
                return False
            lado = "izquierdo" if clave < nodo.clave else "derecho"
            siguiente = getattr(nodo, lado)
            if siguiente is None:
                setattr(nodo, lado, _Nodo(clave, valor))
                self._cantidad += 1
                return True
            nodo = siguiente

    def buscar(self, clave):
        nodo = self.raiz
        while nodo is not None:
            if clave == nodo.clave:
                return nodo.valor
            nodo = nodo.izquierdo if clave < nodo.clave else nodo.derecho
        return None

    def eliminar(self, clave):
        self.raiz, eliminado = self._eliminar(self.raiz, clave)
        if eliminado:
            self._cantidad -= 1
        return eliminado

    def _eliminar(self, nodo, clave):
        if nodo is None:
            return None, False
        if clave < nodo.clave:
            nodo.izquierdo, eliminado = self._eliminar(nodo.izquierdo, clave)
            return nodo, eliminado
        if clave > nodo.clave:
            nodo.derecho, eliminado = self._eliminar(nodo.derecho, clave)
            return nodo, eliminado
        if nodo.izquierdo is None:
            return nodo.derecho, True
        if nodo.derecho is None:
            return nodo.izquierdo, True
        sucesor = nodo.derecho
        while sucesor.izquierdo is not None:
            sucesor = sucesor.izquierdo
        nodo.clave, nodo.valor = sucesor.clave, sucesor.valor
        nodo.derecho, _ = self._eliminar(nodo.derecho, sucesor.clave)
        return nodo, True

    def en_orden(self):
        resultado = []
        pila = []
        nodo = self.raiz
        while pila or nodo is not None:
            while nodo is not None:
                pila.append(nodo)
                nodo = nodo.izquierdo
            nodo = pila.pop()
            resultado.append((nodo.clave, nodo.valor))
            nodo = nodo.derecho
        return resultado
