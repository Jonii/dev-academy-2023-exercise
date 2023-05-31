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

type StationDataSchema = {
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

const exampleStats = [{"date":"2021-05-22","Departure station name":"Hanasaari","Return station name":"Mellstenintie","Count":8}];

type DailyStats = {
    date: string;
    "Departure station name": string;
    "Return station name": string;
    Count: number;
}

export type { StationDataSchema, BikeTrip, BikeTripRaw, DailyStats };