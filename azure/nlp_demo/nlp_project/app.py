"""Interactive Azure Text Analytics dashboard with animated UI."""

from __future__ import annotations

import streamlit as st
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


st.set_page_config(
    page_title="Neon NLP Studio",
    page_icon="🎨",
    layout="wide",
)


def inject_styles() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Syne:wght@600;700;800&display=swap');

        .stApp {
            background: radial-gradient(circle at 20% 20%, #12243a 0%, #0f1624 35%, #070b13 100%);
            font-family: 'Space Grotesk', sans-serif;
            color: #ecf2ff;
        }

        .hero {
            position: relative;
            overflow: hidden;
            border-radius: 24px;
            padding: 26px 28px;
            margin-bottom: 14px;
            background: linear-gradient(130deg, rgba(32, 182, 255, 0.18), rgba(255, 146, 83, 0.18));
            border: 1px solid rgba(255, 255, 255, 0.16);
            box-shadow: 0 18px 34px rgba(0, 0, 0, 0.36);
            animation: reveal 700ms ease-out;
        }

        .hero h1 {
            margin: 0;
            font-family: 'Syne', sans-serif;
            font-weight: 800;
            letter-spacing: 0.4px;
            color: #f6fbff;
            font-size: 2rem;
        }

        .hero p {
            margin: 8px 0 0 0;
            opacity: 0.95;
        }

        .orb {
            position: absolute;
            border-radius: 100%;
            filter: blur(2px);
            opacity: 0.35;
            animation: floaty 7s ease-in-out infinite;
        }

        .orb.one {
            width: 150px;
            height: 150px;
            background: #22d3ee;
            right: -20px;
            top: -20px;
        }

        .orb.two {
            width: 110px;
            height: 110px;
            background: #fb923c;
            right: 130px;
            bottom: -30px;
            animation-delay: 0.7s;
        }

        .glass {
            border-radius: 18px;
            border: 1px solid rgba(255, 255, 255, 0.14);
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.12), rgba(255, 255, 255, 0.05));
            padding: 18px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
            animation: reveal 500ms ease-out;
        }

        .chip {
            display: inline-block;
            margin: 6px 8px 2px 0;
            padding: 6px 12px;
            border-radius: 999px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            background: rgba(12, 39, 58, 0.65);
            color: #eaf8ff;
            font-size: 0.85rem;
            animation: pop 260ms ease-out;
        }

        .entity {
            border-left: 4px solid #22d3ee;
            padding: 8px 10px;
            margin-bottom: 8px;
            border-radius: 8px;
            background: rgba(20, 38, 62, 0.7);
        }

        .score-row {
            margin-top: 8px;
        }

        .score-label {
            font-size: 0.9rem;
            margin-bottom: 2px;
            color: #dbeafe;
        }

        .score-track {
            width: 100%;
            height: 9px;
            background: rgba(255, 255, 255, 0.14);
            border-radius: 999px;
            overflow: hidden;
        }

        .score-bar {
            height: 100%;
            border-radius: 999px;
            animation: fill 1100ms ease-out;
        }

        .footer-note {
            opacity: 0.8;
            font-size: 0.9rem;
            margin-top: 8px;
        }

        @keyframes floaty {
            0%, 100% { transform: translateY(0px) translateX(0px); }
            50% { transform: translateY(-14px) translateX(-6px); }
        }

        @keyframes reveal {
            from { transform: translateY(10px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }

        @keyframes pop {
            from { transform: scale(0.88); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
        }

        @keyframes fill {
            from { width: 0%; }
            to { width: 100%; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero() -> None:
    st.markdown(
        """
        <div class="hero">
            <div class="orb one"></div>
            <div class="orb two"></div>
            <h1>Neon NLP Studio</h1>
            <p>Analyze language, sentiment, entities, key phrases, and PII with animated visual insights.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def score_bar(label: str, value: float, color: str) -> None:
    safe_value = max(0.0, min(1.0, value))
    st.markdown(
        f"""
        <div class="score-row">
            <div class="score-label">{label}: {safe_value:.0%}</div>
            <div class="score-track">
                <div class="score-bar" style="width:{safe_value * 100:.2f}%; background:{color};"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def make_client(endpoint: str, key: str) -> TextAnalyticsClient:
    return TextAnalyticsClient(endpoint=endpoint.strip(), credential=AzureKeyCredential(key.strip()))


inject_styles()
render_hero()

st.sidebar.markdown("## Azure Connection")
endpoint = st.sidebar.text_input("Endpoint", placeholder="https://<resource>.cognitiveservices.azure.com/")
api_key = st.sidebar.text_input("API key", type="password")

st.sidebar.markdown("---")
st.sidebar.markdown("## Sample Inputs")
sample_choice = st.sidebar.selectbox(
    "Choose sample",
    ["Custom", "Product Review", "Customer Feedback", "News Update", "Social Post", "PII Example"],
)

samples = {
    "Product Review": "I absolutely love this product! The build quality is excellent and delivery was fast.",
    "Customer Feedback": "The service was polite, but support response time was slow and frustrating.",
    "News Update": "A major AI startup opened a new office in Seattle and announced a multilingual assistant.",
    "Social Post": "This launch event is incredible. The demos were clean, fast, and super practical!",
    "PII Example": "Hi, I am Maria. My email is maria84@contoso.com and my phone is 555-123-9911.",
}

default_text = "" if sample_choice == "Custom" else samples[sample_choice]

input_col, output_col = st.columns([1, 1.2])

with input_col:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.subheader("Text Input")
    user_text = st.text_area(
        "Enter text",
        value=default_text,
        height=260,
        placeholder="Paste any sentence, paragraph, or social post to analyze.",
    )
    st.caption(f"Characters: {len(user_text)}")
    analyze = st.button("Analyze With Azure AI", type="primary", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with output_col:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.subheader("Visual Insights")

    if analyze:
        if not endpoint or not api_key or not user_text.strip():
            st.warning("Add endpoint, API key, and input text to run analysis.")
        else:
            with st.spinner("Running language intelligence pipeline..."):
                try:
                    client = make_client(endpoint, api_key)
                    documents = [user_text.strip()]

                    sentiment_result = client.analyze_sentiment(documents=documents)[0]
                    phrases_result = client.extract_key_phrases(documents=documents)[0]
                    language_result = client.detect_language(documents=documents)[0]
                    entity_result = client.recognize_entities(documents=documents)[0]
                    pii_result = client.recognize_pii_entities(documents=documents)[0]

                    if any(
                        result.is_error
                        for result in [
                            sentiment_result,
                            phrases_result,
                            language_result,
                            entity_result,
                            pii_result,
                        ]
                    ):
                        st.error("One or more Azure operations returned an error. Try shorter text or verify your key.")
                    else:
                        st.markdown("### Sentiment Pulse")
                        emoji_map = {
                            "positive": "😊",
                            "neutral": "😐",
                            "negative": "😞",
                            "mixed": "🤹",
                        }
                        st.markdown(
                            f"## {emoji_map.get(sentiment_result.sentiment, '🧠')} {sentiment_result.sentiment.title()}"
                        )

                        score_bar("Positive", sentiment_result.confidence_scores.positive, "#34d399")
                        score_bar("Neutral", sentiment_result.confidence_scores.neutral, "#93c5fd")
                        score_bar("Negative", sentiment_result.confidence_scores.negative, "#fb7185")

                        st.markdown("---")
                        st.markdown("### Language Detection")
                        lang_name = language_result.primary_language.name
                        lang_score = language_result.primary_language.confidence_score
                        st.metric("Detected language", lang_name, f"{lang_score:.0%} confidence")

                        st.markdown("---")
                        st.markdown("### Key Phrases")
                        if phrases_result.key_phrases:
                            chips = "".join(
                                [f'<span class="chip">{phrase}</span>' for phrase in phrases_result.key_phrases]
                            )
                            st.markdown(chips, unsafe_allow_html=True)
                        else:
                            st.info("No key phrases found.")

                        st.markdown("---")
                        st.markdown("### Named Entities")
                        if entity_result.entities:
                            for entity in entity_result.entities[:10]:
                                st.markdown(
                                    f"""
                                    <div class="entity">
                                        <strong>{entity.text}</strong><br/>
                                        Category: {entity.category} | Subcategory: {entity.subcategory or 'N/A'} | Confidence: {entity.confidence_score:.2f}
                                    </div>
                                    """,
                                    unsafe_allow_html=True,
                                )
                        else:
                            st.info("No entities found.")

                        st.markdown("---")
                        st.markdown("### PII Redaction")
                        st.code(pii_result.redacted_text)
                        if pii_result.entities:
                            st.write(
                                [
                                    {
                                        "text": item.text,
                                        "category": item.category,
                                        "score": round(item.confidence_score, 3),
                                    }
                                    for item in pii_result.entities
                                ]
                            )
                            st.balloons()
                        else:
                            st.success("No PII entities detected in this text.")

                except Exception as ex:
                    st.error(f"Analysis failed: {ex}")
    else:
        st.info("Run analysis to see animated results and graphics.")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    '<p class="footer-note">Tip: Use realistic, multi-sentence text for richer entity and phrase extraction.</p>',
    unsafe_allow_html=True,
)