from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

preprocessor = ColumnTransformer(
    transformers=[
        (
            "onehot_encoder",
            OneHotEncoder(sparse_output=False, handle_unknown="ignore"),
            ['gender', 'platform_usage']
        ),
        (
            "ordinal_encoder",
            OrdinalEncoder(),
            ['social_interaction_level'],
        )
    ],
    remainder="passthrough"
)