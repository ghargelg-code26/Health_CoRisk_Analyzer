import pandas as pd
import plotly.express as px
import streamlit as st


DATA_PATH = "Datasets/Patient_Comorbidity_Risk_Assessment_Dataset.csv"

CHART_PALETTE = ["#ff6384", "#ff9f40", "#36a2eb", "#9966ff", "#4bc0c0"]
BMI_COLORS = {
    "Underweight": "#36a2eb",
    "Normal weight": "#4bc0c0",
    "Overweight": "#ff9f40",
    "Obese": "#ff6384",
    "Unknown": "#9966ff",
}
SMOKING_COLORS = {
    "Never": "#4bc0c0",
    "Former": "#36a2eb",
    "Current": "#ff6384",
    "Unknown": "#9966ff",
}
DIABETES_COLORS = {0: "#36a2eb", 1: "#ff6384", "0": "#36a2eb", "1": "#ff6384"}


st.set_page_config(page_title="Health_CoRisk_Analyzer", page_icon="🩺", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #07131f 0%, #0a1b2a 35%, #102a3f 100%);
        color: #eaf3ff;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    div[data-testid="stSidebar"] > div:first-child {
        background: rgba(10, 22, 35, 0.92);
        border-right: 1px solid rgba(130, 163, 196, 0.2);
    }
    h1, h2, h3 {
        color: #f2f7ff !important;
    }
    .stMetric {
        background: rgba(17, 35, 51, 0.85);
        border: 1px solid rgba(148, 180, 216, 0.22);
        border-radius: 12px;
        padding: 0.7rem 0.9rem;
        box-shadow: 0 8px 18px rgba(0,0,0,0.12);
    }
    .metric-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 1rem;
        margin: 1rem 0 1.5rem 0;
    }
    .metric-card {
        border-radius: 16px;
        padding: 1rem 1.1rem;
        min-height: 120px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        border: 1px solid rgba(255,255,255,0.12);
        box-shadow: 0 10px 28px rgba(0,0,0,0.18);
    }
    .metric-card h4 {
        margin: 0;
        font-size: 0.8rem;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        opacity: 0.92;
    }
    .metric-card .metric-value {
        margin-top: 0.5rem;
        font-size: 2.1rem;
        font-weight: 800;
        line-height: 1.15;
    }
    .metric-red {
        background: linear-gradient(135deg, rgba(255, 99, 132, 0.25), rgba(255, 159, 64, 0.2));
        border-color: rgba(255, 122, 122, 0.55);
    }
    .metric-orange {
        background: linear-gradient(135deg, rgba(255, 159, 64, 0.25), rgba(253, 203, 110, 0.2));
        border-color: rgba(255, 192, 92, 0.55);
    }
    .metric-blue {
        background: linear-gradient(135deg, rgba(54, 162, 235, 0.25), rgba(75, 192, 192, 0.2));
        border-color: rgba(112, 184, 255, 0.55);
    }
    .metric-purple {
        background: linear-gradient(135deg, rgba(153, 102, 255, 0.25), rgba(201, 115, 255, 0.2));
        border-color: rgba(182, 132, 255, 0.55);
    }
    .metric-label {
        color: #b8d3f2 !important;
    }
    .metric-value {
        color: #fff !important;
    }
    .stDataFrame {
        background: rgba(11, 24, 34, 0.9);
        border-radius: 10px;
    }
    .stAlert {
        background: rgba(18, 42, 60, 0.75);
        border: 1px solid rgba(143, 189, 255, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    """Load the patient dataset and add derived risk-analysis features."""
    df = pd.read_csv(path)

    def bmi_category(bmi):
        """Classify a BMI value into a standard category."""
        if pd.isna(bmi):
            return "Unknown"
        if bmi < 18.5:
            return "Underweight"
        if bmi < 25:
            return "Normal weight"
        if bmi < 30:
            return "Overweight"
        return "Obese"

    df["BMI_Category"] = df["BMI"].apply(bmi_category)
    df["Smoking_current"] = df["Smoking_Status"].fillna("Unknown").str.lower().eq("current").astype(int)
    df["SBP_high"] = (df["Systolic_BP"] >= 140).astype(int)
    df["Low_Adherence"] = (df["Medication_Adherence_Percentage"] < 80).astype(int)
    df["Obesity_Flag"] = (df["BMI_Category"] == "Obese").astype(int)
    df["Family_History_Flag"] = df["Family_History_CVD"].fillna(0).astype(int)
    df["Obesity_x_FH"] = df["Obesity_Flag"] * df["Family_History_Flag"]
    return df




def main():
    """Render the Streamlit dashboard and apply the selected patient filters."""
    st.markdown(
        """
        <div style="padding: 1rem 0 1.5rem 0; border-left: 4px solid #5ba8ff; background: rgba(18, 36, 52, 0.7); border-radius: 14px; padding-left: 1.2rem; margin-bottom: 1rem;">
            <h1 style="margin: 0; font-size: 2.3rem; font-weight: 800;">Educational Dashboard Using Synthetic Healthcare Data for learning purpose</h1>
            <p style="margin: 0.5rem 0 0 0; color: #cfe0f9; font-size: 1.02rem;">
                Cardiovascular risk intelligence dashboard for fast decision support and business-facing insight generation.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    df = load_data(DATA_PATH)

    st.sidebar.header("Filters")
    gender_options = sorted(df["Gender"].dropna().unique().tolist())
    smoking_options = sorted(df["Smoking_Status"].dropna().unique().tolist())

    selected_gender = st.sidebar.multiselect("Gender", gender_options, default=gender_options)
    selected_smoking = st.sidebar.multiselect("Smoking Status", smoking_options, default=smoking_options)
    include_family_history = st.sidebar.checkbox("Patients with family history only", value=False)
    include_diabetes = st.sidebar.checkbox("Patients with diabetes only", value=False)

    filtered = df[
        df["Gender"].isin(selected_gender)
        & df["Smoking_Status"].isin(selected_smoking)
    ].copy()

    if include_family_history:
        filtered = filtered[filtered["Family_History_CVD"] == 1]
    if include_diabetes:
        filtered = filtered[filtered["Diabetes"] == 1]

    if filtered.empty:
        st.warning("No records match the selected criteria. Please adjust the filters.")
        return

    filtered = filtered.copy()
    filtered["BMI_for_size"] = pd.to_numeric(filtered["BMI"], errors="coerce").fillna(filtered["BMI"].median())

    heart_attack_avg = filtered["Heart_Attack_Risk_Percentage"].mean()
    mortality_avg = filtered["Mortality_Risk_Percentage"].mean()
    high_bp_share = (filtered["SBP_high"] == 1).mean() * 100
    low_adherence_share = (filtered["Low_Adherence"] == 1).mean() * 100

    st.subheader("Executive Summary")
    st.markdown(
        "This dashboard identifies the patient groups most likely to be affected by elevated cardiovascular risk and surfaces the strongest intervention signals across the dataset. "
        "It supports rapid decision-making for prevention, monitoring, and resource allocation in a business-facing healthcare context."
    )

    st.markdown(
        f"""
        <div class="metric-grid">
            <div class="metric-card metric-red">
                <h4>Avg Heart Attack Risk</h4>
                <div class="metric-value">{heart_attack_avg:.1f}%</div>
            </div>
            <div class="metric-card metric-orange">
                <h4>Avg Mortality Risk</h4>
                <div class="metric-value">{mortality_avg:.1f}%</div>
            </div>
            <div class="metric-card metric-blue">
                <h4>High Systolic BP</h4>
                <div class="metric-value">{high_bp_share:.1f}%</div>
            </div>
            <div class="metric-card metric-purple">
                <h4>Low Adherence</h4>
                <div class="metric-value">{low_adherence_share:.1f}%</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Risk Analysis by Key Health Factors")
    col_left, col_right = st.columns(2)

    bmi_summary = (
        filtered.groupby("BMI_Category", dropna=False)[["Heart_Attack_Risk_Percentage", "Mortality_Risk_Percentage"]]
        .mean()
        .reset_index()
    )
    fig_bmi = px.bar(
        bmi_summary,
        x="BMI_Category",
        y="Heart_Attack_Risk_Percentage",
        color="BMI_Category",
        color_discrete_map=BMI_COLORS,
        title="Average Heart Attack Risk by BMI Category",
        labels={"BMI_Category": "BMI Category", "Heart_Attack_Risk_Percentage": "Avg Heart Attack Risk (%)"},
    )
    fig_bmi.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        title_font=dict(color="#4bc0c0", size=19),
    )
    col_left.plotly_chart(fig_bmi, use_container_width=True)

    smoking_summary = (
        filtered.groupby("Smoking_Status")["Heart_Attack_Risk_Percentage"]
        .mean()
        .reset_index()
        .sort_values("Heart_Attack_Risk_Percentage", ascending=False)
    )
    fig_smoke = px.bar(
        smoking_summary,
        x="Smoking_Status",
        y="Heart_Attack_Risk_Percentage",
        color="Smoking_Status",
        color_discrete_map=SMOKING_COLORS,
        title="Heart Attack Risk by Smoking Status",
        labels={"Smoking_Status": "Smoking Status", "Heart_Attack_Risk_Percentage": "Avg Heart Attack Risk (%)"},
    )
    fig_smoke.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        title_font=dict(color="#ff9f40", size=19),
    )
    col_right.plotly_chart(fig_smoke, use_container_width=True)

    col_a, col_b = st.columns(2)

    family_summary = (
        filtered.groupby("Family_History_CVD")["Heart_Attack_Risk_Percentage"]
        .mean()
        .reset_index()
    )
    family_summary["Family_History_CVD"] = family_summary["Family_History_CVD"].map({0: "No", 1: "Yes"})
    fig_family = px.bar(
        family_summary,
        x="Family_History_CVD",
        y="Heart_Attack_Risk_Percentage",
        color="Family_History_CVD",
        color_discrete_map={"No": "#36a2eb", "Yes": "#ff6384"},
        title="Heart Attack Risk by Family History of CVD",
        labels={"Family_History_CVD": "Family History of CVD", "Heart_Attack_Risk_Percentage": "Avg Heart Attack Risk (%)"},
    )
    fig_family.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        title_font=dict(color="#ff6384", size=19),
    )
    col_a.plotly_chart(fig_family, use_container_width=True)

    scatter = px.scatter(
        filtered,
        x="Systolic_BP",
        y="Mortality_Risk_Percentage",
        color="Diabetes",
        color_discrete_map=DIABETES_COLORS,
        color_discrete_sequence=CHART_PALETTE,
        size="BMI_for_size",
        hover_name="Patient_ID",
        title="Systolic Blood Pressure vs Mortality Risk",
        labels={
            "Systolic_BP": "Systolic BP",
            "Mortality_Risk_Percentage": "Mortality Risk (%)",
            "Diabetes": "Diabetes",
            "BMI_for_size": "BMI",
        },
    )
    scatter.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        title_font=dict(color="#9966ff", size=19),
    )
    col_b.plotly_chart(scatter, use_container_width=True)

    st.subheader("Business Recommendations")
    st.markdown(
        """
        - Prioritise patients with high BMI and smoking exposure for preventive intervention review.
        - Focus risk education and monitoring on patients with elevated systolic blood pressure.
        - Investigate low medication adherence as a key operational risk factor for poorer outcomes.
        - Use family history and diabetes status to target population-level preventative programmes.
        """
    )

    st.subheader("Data Preview")
    st.dataframe(filtered.head(15), use_container_width=True)

    st.markdown("---")
    st.caption("Health_CoRisk_Analyzer | Data App Prototype | Risk Intelligence Dashboard")


if __name__ == "__main__":
    main()
