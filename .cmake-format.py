# ----------------------------------------
# Settings controlling listfile parsing
# ----------------------------------------
with section("parse_settings"):

    # Define configuration for custom cmake functions
    custom_commands = {
        'FetchContent_Declare': {
            'flags': ['OVERRIDE_FIND_PACKAGE'],
            'parameters': {
                'URL': '*',
                'URL_HASH': '*',
                'DOWNLOAD_EXTRACT_TIMESTAMP': '*',
                'GIT_REPO': '*',
                'GIT_TAG': '*'
            }
        },
        'create_gtest_target': {
            'flags': [],
            'parameters': {
                'TEST_NAME': '*',
                'TEST_SOURCE': '*',
                'INCLUDE_DIR': '*'
            }
        },
        'create_protobuf_target_for_proto_path': {
            'flags': [],
            'parameters': {
                'TARGET': '*',
                'PROTO_DIR': '*',
                'OUTPUT_DIR': '*',
                'DEPENDENCIES': '*',
                'EXTRA_OPTIONS': '*'
            }
        },
        'create_protobuf_target_for_one_proto_file': {
            'flags': [],
            'parameters': {
                'TARGET': '*',
                'PROTO_FILE': '*',
                'OUTPUT_DIR': '*',
                'DEPENDENCIES': '*',
                'EXTRA_OPTIONS': '*'
            }
        },
        'create_protobuf_aimrt_rpc_for_proto_files': {
            'flags': [],
            'parameters': {
                'TARGET': '*',
                'PROTO_FILES': '*',
                'OUTPUT_DIR': '*',
                'DEPENDENCIES': '*',
                'EXTRA_OPTIONS': '*'
            }
        },
        'create_ros2_aimrt_rpc_for_single_file': {
            'flags': [],
            'parameters': {
                'PACKAGE': '*',
                'PROTO_FILE': '*',
                'OUTPUT_DIR': '*',
                'DEPENDENCIES': '*',
                'EXTRA_OPTIONS': '*'
            }
        }
    }

    # Override settings for specific commands where applicable
    override_rules = {}

    # Define variable tags
    variable_tags = []

    # Define property tags
    property_tags = []

# -------------------------------------
# Settings affecting code formatting
# -------------------------------------
with section("formatting"):

    # Maximum width for formatted CMake files
    max_line_length = 180

    # Number of spaces used for indentation
    indent_size = 2

    # Threshold for horizontal wrapping of sub-groups within argument groups
    max_subgroups_wrap = 2

    # Threshold for horizontal wrapping of positional arguments
    max_arguments_wrap = 6

    # Limit of lines for a command-line argument group before forcing nesting
    max_cmdline_rows = 2

    # Whether to add space between control names and parentheses
    add_space_after_ctrl = False

    # Whether to add space between function names and parentheses
    add_space_after_fn = False

    # Dangle closing parentheses on a new line when wrapping
    dangle_closing_paren = False

    # Commands that should always trigger wrapping
    wrap_always = [
        'target_link_libraries/PUBLIC/Arguments[0]',
        'target_link_libraries/PRIVATE/Arguments[0]',
        'target_link_libraries/INTERFACE/Arguments[0]',
        'target_include_directories/PUBLIC/Arguments[0]',
        'target_include_directories/PRIVATE/Arguments[0]',
        'target_include_directories/INTERFACE/Arguments[0]',
        'add_custom_target/DEPENDENCIES/Arguments[0]',
        'create_protobuf_target_for_proto_path/DEPENDENCIES/Arguments[0]',
        'create_protobuf_target_for_one_proto_file/DEPENDENCIES/Arguments[0]',
        'create_protobuf_aimrt_rpc_for_proto_files/DEPENDENCIES/Arguments[0]',
        'create_ros2_aimrt_rpc_for_single_file/DEPENDENCIES/Arguments[0]'
    ]

# -------------------------------------------------
# Settings for comment formatting and reflow
# -------------------------------------------------
with section("comment_settings"):

    # Character used for bullet points in lists
    bullet_character = '*'

    # Character used after numerals in enumerated lists
    numeral_punctuation = '.'

    # Keep formatting of the first comment block (e.g., for licenses)
    keep_first_comment_literal = False

    # Regex pattern to match comments that should not be reformatted
    ignore_comment_pattern = None

    # Regex pattern for matching preformatted code fences
    preformat_fence_regex = r'^\s*([`~]{3}[`~]*)(.*)$'

    # Regex pattern for matching ruler lines
    ruler_line_regex = r'^\s*[^\\w\\s]{3}.*[^\\w\\s]{3}$'

    # Pattern to match trailing comments, defaulting to '#<'
    trailing_comment_pattern = '#<'

    # Minimum length of consecutive hash characters to preserve in comment rulers
    min_hashruler_length = 10

    # Normalize hash ruler lengths and add space after the first hash
    normalize_hashrulers = True

    # Enable reflow and markup processing for comments
    enable_comment_markup = False
