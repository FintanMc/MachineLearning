from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

def preprocessor(remainder="passthrough"):

    transformers = [
        (
            "onehot_encoder",
            OneHotEncoder(sparse_output=False, handle_unknown="ignore"),
            ['gender', 'platform_usage']
        ),
        (
            "ordinal_encoder",
            OrdinalEncoder(),
            ['social_interaction_level'],
        ),
    ]

    if remainder == "drop":
        transformers.append(
            (
                "keep",
                "passthrough",
                ["daily_social_media_hours", "stress_level", "anxiety_level", "sleep_hours"]
            )
        )

    return ColumnTransformer(
        transformers=transformers,
        remainder=remainder
    )