type BikeTrip = {
    Departure: Date;
    Return: Date;
    "Departure station id": number;
    "Departure station name": string;
    "Return station id": number;
    "Return station name": string;
    "Covered distance (m)": number;
    "Duration (sec.)": number;
};
type BikeTripRaw = {
    trips: {
        Departure: string;
        Return: string;
        "Departure station id": number;
        "Departure station name": string;
        "Return station id": number;
        "Return station name": string;
        "Covered distance (m)": number;
        "Duration (sec.)": number;
    }[];
    pages: number;
    start_time: string;
}

type stationDataSchema = {
    FID: number,
    ID: number,
    Nimi: String,
    Namn: String,
    Name: String,
    Osoite: String,
    Adress: String,
    Kaupunki: String,
    Stad: String,
    Operaattor: String,
    Kapasiteet: number,
    x: number,
    y: number
}

export type { stationDataSchema, BikeTrip, BikeTripRaw };