class Hotel {
    constructor(nomeHotel, cidade, quartosDisponiveisHotel) {
        this.nomeHotel = nomeHotel;
        this.cidade = cidade;
        this.quartosDisponiveisHotel = quartosDisponiveisHotel;
        this.historicoReservas = []; // Lista para armazenar as reservas feitas
    }

    reservarQuarto(cliente) {
        // Verifica se há quartos disponíveis
        if (this.quartosDisponiveisHotel > 0) {
            this.quartosDisponiveisHotel--; // Diminui o número de quartos disponíveis
            // Adiciona a reserva ao histórico do cliente
            this.historicoReservas.push({
                cliente: cliente.nomeCliente,
                cpf: cliente.cpfCliente,
                data: new Date().toLocaleString() // Registra a data da reserva
            });
            console.log(`Reserva confirmada para ${cliente.nomeCliente} no ${this.nomeHotel}.`);
            return true; // Retorna verdadeiro para indicar que a reserva foi bem-sucedida
        } else {
            console.log("Não foi possível realizar a reserva. Quartos indisponíveis.");
            return false; // Retorna falso se não houver quartos disponíveis
        }
    }

    cancelarReserva(cliente) {
        // A lógica de cancelamento não está implementada, mas uma possível implementação poderia ser aqui
        // Para simplificação, você precisaria armazenar quando estava reservando e como cancelar.
        console.log(`Reserva cancelada para ${cliente.nomeCliente}.`);
        this.quartosDisponiveisHotel++; // Adiciona um quarto de volta
        // Aqui você deve remover a reserva do histórico do hotel
    }
}
class Cliente {
    constructor(nomeCliente, cpfCliente) {
        this.nomeCliente = nomeCliente;
        this.cpfCliente = cpfCliente;
        this.historicoReservas = []; // Inicializa uma lista vazia para o histórico de reservas
    }

    adicionarReserva(hotel) {
        // Este método adiciona uma reserva ao histórico do cliente
        this.historicoReservas.push({
            hotel: hotel.nomeHotel,
            data: new Date().toLocaleString() // Registra a data da reserva
        });
    }

    visualizarHistorico() {
        // Método para visualizar o histórico de reservas do cliente
        console.log(`Histórico de Reservas de ${this.nomeCliente}:`);
        if (this.historicoReservas.length === 0) {
            console.log("Nenhuma reserva encontrada.");
        } else {
            this.historicoReservas.forEach(reserva => {
                console.log(`- Hotel: ${reserva.hotel}, Data: ${reserva.data}`);
            });
        }
    }
}

// Exemplo de uso
const hotel1 = new Hotel("Hotel Maravilha", "Rio de Janeiro");
const cliente1 = new Cliente("João Silva", "123.456.789-00");

// O cliente tenta reservar um quarto
if (hotel1.reservarQuarto(cliente1)) {
    cliente1.adicionarReserva(hotel1); // Adiciona a reserva ao histórico do cliente
}

// O cliente visualiza seu histórico de reservas
cliente1.visualizarHistorico();
