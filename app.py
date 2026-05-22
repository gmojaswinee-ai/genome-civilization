import streamlit as st
import random

st.title("🧬 Genome Civilization Simulator")

# ---------- CORE FUNCTIONS ----------

def generate_genome(length=10):
    return ''.join(random.choice("ATGC") for _ in range(length))

def mutate(genome):
    genome = list(genome)
    idx = random.randint(0, len(genome)-1)
    genome[idx] = random.choice("ATGC")
    return ''.join(genome)

def mutation_pressure(genome):
    return sum(1 for i in genome if i in "GC") / len(genome)

def classify_state(score):
    if score > 0.6:
        return "🔥 Chaotic"
    elif score > 0.3:
        return "⚖ Balanced"
    else:
        return "🌱 Stable"

# ---------- UI ----------

if "genome" not in st.session_state:
    st.session_state.genome = generate_genome()

st.write("### Current Genome")
st.code(st.session_state.genome)

if st.button("Mutate"):
    st.session_state.genome = mutate(st.session_state.genome)

if st.button("Analyze"):
    score = mutation_pressure(st.session_state.genome)
    state = classify_state(score)

    st.write("### Mutation Pressure")
    st.write(score)

    st.write("### State")
    st.success(state)

if st.button("Reset Genome"):
    st.session_state.genome = generate_genome()
