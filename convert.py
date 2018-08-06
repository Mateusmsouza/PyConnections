class ToolKitms(object):


    def converte(self, componentes):
        try:

            inicio = componentes[2]
            final = componentes [4]
            h1, m1,s1 = inicio.split(":")
            h2, m2,s2 = final.split(":")

            segundos_inicio = self.__make_it_second(h1,m1,s1)
            segundos_final = self.__make_it_second(h2,m2,s2)
            segundos_total = segundos_final - segundos_inicio
            return "Tempo de acesso: [{}] ".format(self.__constroi_hora(segundos_total)) + "ID acessada: {} ".format(componentes[0]) + "Data: {} ".format(componentes[1]) + "Tipo de Conexão: {}".format(componentes[6])
        except:
            return "Calculo Falhou. Isso pode ter ocorrido pois a linha não continha valores inteiros."

    def __constroi_hora(self, segundos):
        horas = int((segundos -(segundos % 3600))/3600)
        segundos = int((segundos % 3600))
        minutos = int((segundos -(segundos % 60))/60)
        segundos = int((segundos % 60))

        if len(str(horas)) == 1:horas = '0'+str(horas)
        if len(str(minutos)) == 1:minutos = '0'+str(minutos)
        if len(str(segundos)) == 1 :segundos = '0'+str(segundos)

        return str(horas)+':'+str(minutos)+':'+str(segundos)

    def __make_it_second(self,h,m,s):
        return ((int(h) * 3600) + (int(m) * 60) + int(s))

    def add(self,time, adicional_time):
        h, m, s = adicional_time.split(":")
        adicional_time = self.__make_it_second(h,m,s)
        if time:
            h, m, s = time.split(":")
            time = self.__make_it_second(h,m,s)
        else:
            time = 0

        print(self.__constroi_hora(time+adicional_time))
        return self.__constroi_hora(time+adicional_time)
