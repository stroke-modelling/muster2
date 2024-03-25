# Stroke Pathway Model with MSUs (Determinstic model per LSOA)

Simpy pathway model for stroke thrombolysis and thrombectomy. This models compares the outcome difference between two models of care:

## Models of care

### Drip and Shaip

```mermaid
flowchart LR
    A[Stroke\nonset] --> |Delay| B(Call 999)
    B --> |Delay| C(Ambulance\ndispatch + travel)
    C --> D(Ambulance\non-scene)
    D --> E{Use closest\nunit}
    E --> |Travel| F(IVT-Only)
    E --> |Travel| G(IVT/MT Unit)
    F .-> |Transfer\nif required| G
    G --> H[Outcome]
    F --> H
```

### Mothership

```mermaid
flowchart LR
    A[Stroke\nonset] --> |Delay| B(Call 999)
    B --> |Delay| C(Ambulance\ndispatch + travel)
    C --> D(Ambulance\non-scene)
    D --> E{Use closest\n MT unit}
    E --> |Travel| G(IVT/MT Unit)
    G --> H[Outcome]
    F --> H
```

### Pre-hopsital diagnosis

```mermaid
flowchart LR
    A[Stroke\nonset] --> |Delay| B(Call 999)
    B --> |Delay| C(Ambulance\ndispatch + travel)
    C --> D(Ambulance\non-scene)
    D --> E{Pre-hopsital\ndiagnosis}
    E --> |Travel| F(IVT-only Unit)
    E --> |Travel| G(IVT/MT Unit)
    F .-> |Transfer\nif required| G
    G --> H[Outcome]
    F --> H
```


### Mobile Stroke Unit (MSU)

```mermaid
flowchart LR
    A[Stroke\nonset] --> |Delay| B(Call 999)
    B --> |Delay| C(MSU dispatch\n+ travel)
    C --> D(MSU\non-scene)
    D --> E(On-scene IVT)
    E --> G |Travel| (MT Unit)
    G --> H[Outcome]
    F --> H
```