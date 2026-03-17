# Data Dictionary

Source: [AACT (Aggregate Analysis of ClinicalTrials.gov)](https://aact.ctti-clinicaltrials.org/)

## baseline_counts

Sample sizes at baseline for each study group

Source file: `baseline_counts.txt`
Rows: 230,199

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| count | BIGINT | 0.0% | 41 |  |
| scope | VARCHAR | 0.0% | overall |  |
| units | VARCHAR | 0.0% | Participants |  |
| ctgov_group_code | VARCHAR | 0.0% | BG000 |  |
| result_group_id | BIGINT | 0.0% | 650570635 | Joins to result_groups.id |
| nct_id | VARCHAR | 0.0% | NCT03036215 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 72890180 | Table primary key (auto-increment) |

## baseline_measurements

Demographic and baseline measures by group

Source file: `baseline_measurements.txt`
Rows: 2,808,533

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| calculate_percentage | BOOLEAN | 96.6% | false |  |
| population_description | VARCHAR | 94.6% | Race and Ethnicity were not collected from any participant. |  |
| number_analyzed_units | VARCHAR | 0.0% | Participants |  |
| number_analyzed | BIGINT | 0.1% | 41 |  |
| explanation_of_na | VARCHAR | 99.8% | Summary statistics not reported for N\<3 due to small sample size and partici... |  |
| dispersion_upper_limit | DOUBLE | 97.8% | 60.0 |  |
| dispersion_lower_limit | DOUBLE | 97.8% | 18.0 |  |
| dispersion_value_num | DOUBLE | 89.2% | 15.0 |  |
| dispersion_value | VARCHAR | 89.1% | 15 |  |
| dispersion_type | VARCHAR | 86.9% | STANDARD_DEVIATION |  |
| param_value_num | DOUBLE | 0.3% | 69.0 |  |
| param_value | VARCHAR | 0.1% | 69 |  |
| param_type | VARCHAR | 0.0% | MEAN |  |
| units | VARCHAR | 0.0% | years |  |
| description | VARCHAR | 90.4% | Out of a total of 79 participants, data for baseline measure (age) was availa... |  |
| title | VARCHAR | 0.0% | Age, Continuous |  |
| category | VARCHAR | 35.8% | Female |  |
| classification | VARCHAR | 74.5% | United States |  |
| ctgov_group_code | VARCHAR | 0.1% | BG000 |  |
| result_group_id | BIGINT | 0.1% | 650960813 | Joins to result_groups.id |
| nct_id | VARCHAR | 0.0% | NCT01818141 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 853860309 | Table primary key (auto-increment) |

## brief_summaries

Brief text summary of the study protocol

Source file: `brief_summaries.txt`
Rows: 575,064

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 0.0% | This study is designed to assess and characterize levels of selected harmful ... |  |
| nct_id | VARCHAR | 0.0% | NCT06476405 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 180799380 | Table primary key (auto-increment) |

## browse_conditions

NLM-generated MeSH terms for study conditions

Source file: `browse_conditions.txt`
Rows: 4,194,046

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| mesh_type | VARCHAR | 0.0% | mesh-ancestor |  |
| downcase_mesh_term | VARCHAR | 0.0% | elbow injuries |  |
| mesh_term | VARCHAR | 0.0% | Elbow Injuries |  |
| nct_id | VARCHAR | 0.0% | NCT04642807 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 1266148504 | Table primary key (auto-increment) |

## browse_interventions

NLM-generated MeSH terms for study interventions

Source file: `browse_interventions.txt`
Rows: 2,480,003

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| mesh_type | VARCHAR | 0.0% | mesh-ancestor |  |
| downcase_mesh_term | VARCHAR | 0.0% | cytological techniques |  |
| mesh_term | VARCHAR | 0.0% | Cytological Techniques |  |
| nct_id | VARCHAR | 0.0% | NCT01505699 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 639697671 | Table primary key (auto-increment) |

## calculated_values

AACT-computed fields: months to report results, facilities count, etc.

Source file: `calculated_values.txt`
Rows: 576,029

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| number_of_other_outcomes_to_measure | BIGINT | 91.6% | 1 |  |
| number_of_secondary_outcomes_to_measure | BIGINT | 27.5% | 24 |  |
| number_of_primary_outcomes_to_measure | BIGINT | 3.1% | 2 |  |
| maximum_age_unit | VARCHAR | 46.9% | year |  |
| minimum_age_unit | VARCHAR | 6.6% | year |  |
| maximum_age_num | BIGINT | 46.9% | 99 |  |
| minimum_age_num | BIGINT | 6.6% | 18 |  |
| has_single_facility | BOOLEAN | 10.2% | true |  |
| has_us_facility | BOOLEAN | 10.2% | true |  |
| months_to_report_results | BIGINT | 86.7% | 9 |  |
| were_results_reported | BOOLEAN | 0.0% | false |  |
| actual_duration | BIGINT | 38.8% | 25 |  |
| nlm_download_date | VARCHAR | 100.0% |  |  |
| registered_in_calendar_year | BIGINT | 0.0% | 2021 |  |
| number_of_sae_subjects | BIGINT | 92.9% | 121 |  |
| number_of_nsae_subjects | BIGINT | 90.8% | 9 |  |
| number_of_facilities | BIGINT | 0.0% | 1 |  |
| nct_id | VARCHAR | 0.0% | NCT04966520 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 204876276 | Table primary key (auto-increment) |

## central_contacts

Primary and backup contacts for enrollment questions

Source file: `central_contacts.txt`
Rows: 217,960

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| role | VARCHAR | 0.0% | CONTACT |  |
| phone_extension | VARCHAR | 88.1% | 15571 |  |
| email | VARCHAR | 2.3% | clinicalstudies@cybrexa.com |  |
| phone | VARCHAR | 6.1% | 860-717-2731 |  |
| name | VARCHAR | 0.0% | Clinical Operations Trial Team |  |
| contact_type | VARCHAR | 0.0% | primary |  |
| nct_id | VARCHAR | 0.0% | NCT06315491 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 69409684 | Table primary key (auto-increment) |

## conditions

Disease or condition names studied in each trial

Source file: `conditions.txt`
Rows: 1,025,650

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| downcase_name | VARCHAR | 0.0% | diabetes |  |
| name | VARCHAR | 0.0% | Diabetes |  |
| nct_id | VARCHAR | 0.0% | NCT02729441 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 319326416 | Table primary key (auto-increment) |

## countries

Countries where the study has sites

Source file: `countries.txt`
Rows: 783,722

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| removed | BOOLEAN | 0.0% | true |  |
| name | VARCHAR | 0.0% | United States |  |
| nct_id | VARCHAR | 0.0% | NCT01085357 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 249140304 | Table primary key (auto-increment) |

## design_group_interventions

Cross-reference mapping design groups to interventions

Source file: `design_group_interventions.txt`
Rows: 1,283,125

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| intervention_id | BIGINT | 0.0% | 307040818 | Joins to interventions.id |
| design_group_id | BIGINT | 0.0% | 339966712 | Joins to design_groups.id |
| nct_id | VARCHAR | 0.0% | NCT05097560 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 404345109 | Table primary key (auto-increment) |

## design_groups

Protocol-specified groups or cohorts assigned to interventions

Source file: `design_groups.txt`
Rows: 1,056,031

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 11.8% | A combination of agents will be administered to subjects in this study: Aldox... |  |
| title | VARCHAR | 0.0% | NANT Chordoma Vaccine |  |
| group_type | VARCHAR | 15.4% | EXPERIMENTAL |  |
| nct_id | VARCHAR | 0.0% | NCT03647423 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 340337233 | Table primary key (auto-increment) |

## design_outcomes

Planned outcome measures and observations

Source file: `design_outcomes.txt`
Rows: 3,566,612

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 17.9% | ISTH Major bleed: acute clinically overt bleeding accompanied by one or more ... |  |
| population | VARCHAR | 100.0% |  |  |
| time_frame | VARCHAR | 1.5% | From first dose to first occurrence of event (ISTH major or CRNM bleed) durin... |  |
| measure | VARCHAR | 0.0% | Event Rate of Confirmed Major Bleeding or Clinically Relevant Non-Major Bleed... |  |
| outcome_type | VARCHAR | 0.0% | secondary |  |
| nct_id | VARCHAR | 0.0% | NCT00831441 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 1115106764 | Table primary key (auto-increment) |

## designs

Study design details: allocation, masking, assignment, purpose

Source file: `designs.txt`
Rows: 571,286

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| outcomes_assessor_masked | BOOLEAN | 67.5% | true |  |
| investigator_masked | BOOLEAN | 67.5% | false |  |
| caregiver_masked | BOOLEAN | 67.5% | false |  |
| subject_masked | BOOLEAN | 67.5% | false |  |
| intervention_model_description | VARCHAR | 85.3% | 2-armed, parallel group open label randomised controlled trial. Participants ... |  |
| masking_description | VARCHAR | 92.5% | This study was initially designed as a single center, double-blind, placebo-c... |  |
| masking | VARCHAR | 24.0% | SINGLE |  |
| time_perspective | VARCHAR | 77.0% | CROSS_SECTIONAL |  |
| primary_purpose | VARCHAR | 24.2% | HEALTH_SERVICES_RESEARCH |  |
| observational_model | VARCHAR | 77.5% | CASE_ONLY |  |
| intervention_model | VARCHAR | 24.2% | FACTORIAL |  |
| allocation | VARCHAR | 24.0% | RANDOMIZED |  |
| nct_id | VARCHAR | 0.0% | NCT02839382 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 179581940 | Table primary key (auto-increment) |

## detailed_descriptions

Detailed text description of the study protocol

Source file: `detailed_descriptions.txt`
Rows: 575,064

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 32.6% | Background:~* Patients with germline BRCA1/2 mutations (gBRCAm) demonstrate r... |  |
| nct_id | VARCHAR | 0.0% | NCT03990077 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 181068954 | Table primary key (auto-increment) |

## documents

Full study protocol and statistical analysis plan

Source file: `documents.txt`
Rows: 10,692

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| comment | VARCHAR | 13.6% | For additional information about this study please refer to the GSK Clinical ... |  |
| url | VARCHAR | 0.0% | https://www.clinicalstudydatarequest.com |  |
| document_type | VARCHAR | 0.0% | Clinical Study Report |  |
| document_id | VARCHAR | 15.0% | B2C109575 | Joins to documents.id |
| nct_id | VARCHAR | 0.0% | NCT00600171 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 3514107 | Table primary key (auto-increment) |

## drop_withdrawals

Summary of participant withdrawals: counts and reasons

Source file: `drop_withdrawals.txt`
Rows: 577,923

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| count_units | VARCHAR | 100.0% |  |  |
| reason_comment | VARCHAR | 100.0% |  |  |
| drop_withdraw_comment | VARCHAR | 100.0% |  |  |
| count | BIGINT | 0.0% | 5 |  |
| reason | VARCHAR | 0.0% | Lost to Follow-up |  |
| period | VARCHAR | 0.0% | Overall Study |  |
| ctgov_group_code | VARCHAR | 0.0% | FG000 |  |
| result_group_id | BIGINT | 0.0% | 650534415 | Joins to result_groups.id |
| nct_id | VARCHAR | 0.0% | NCT01256788 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 179875655 | Table primary key (auto-increment) |

## eligibilities

Participant eligibility criteria (inclusion/exclusion, age, sex)

Source file: `eligibilities.txt`
Rows: 575,064

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| older_adult | BOOLEAN | 0.0% | false |  |
| child | BOOLEAN | 0.0% | true |  |
| adult | BOOLEAN | 0.0% | false |  |
| gender_based | BOOLEAN | 96.8% | true |  |
| gender_description | VARCHAR | 97.9% | Treatment of female infertility |  |
| criteria | VARCHAR | 0.0% | Inclusion Criteria:~* Any patient who is 3 to 12 years of age~* Any patient u... |  |
| population | VARCHAR | 77.4% | This study will prospectively collect pregnant women without history of cesar... |  |
| healthy_volunteers | BOOLEAN | 2.3% | false |  |
| maximum_age | VARCHAR | 46.8% | 12 Years |  |
| minimum_age | VARCHAR | 6.4% | 3 Years |  |
| gender | VARCHAR | 0.1% | ALL |  |
| sampling_method | VARCHAR | 77.3% | NON_PROBABILITY_SAMPLE |  |
| nct_id | VARCHAR | 0.0% | NCT01015053 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 180991044 | Table primary key (auto-increment) |

## facilities

Facility names, addresses, and recruiting status

Source file: `facilities.txt`
Rows: 3,410,973

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| longitude | DOUBLE | 2.6% | -81.69541 |  |
| latitude | DOUBLE | 2.6% | 41.4995 |  |
| country | VARCHAR | 0.0% | United States |  |
| zip | VARCHAR | 19.2% | 44106 |  |
| state | VARCHAR | 39.2% | Ohio |  |
| city | VARCHAR | 0.0% | Cleveland |  |
| name | VARCHAR | 6.4% | University Hospitals Cleveland Medical Center, Seidman Cancer Center, Case Co... |  |
| status | VARCHAR | 85.2% | RECRUITING |  |
| nct_id | VARCHAR | 0.0% | NCT05113368 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 1104291733 | Table primary key (auto-increment) |

## facility_contacts

Contact information at each study facility

Source file: `facility_contacts.txt`
Rows: 409,886

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| phone_extension | VARCHAR | 94.4% | 23730 |  |
| phone | VARCHAR | 29.4% | 416-946-4069 |  |
| email | VARCHAR | 29.5% | amy.kirkham@utoronto.ca |  |
| name | VARCHAR | 3.4% | Amy A. Kirkham, PhD |  |
| contact_type | VARCHAR | 0.0% | primary |  |
| facility_id | BIGINT | 0.0% | 1106868321 | Joins to facilities.id |
| nct_id | VARCHAR | 0.0% | NCT06345937 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 139161164 | Table primary key (auto-increment) |

## facility_investigators

Investigator names at each study facility

Source file: `facility_investigators.txt`
Rows: 223,509

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| name | VARCHAR | 0.0% | Xiaolong Fu |  |
| role | VARCHAR | 0.0% | PRINCIPAL_INVESTIGATOR |  |
| facility_id | BIGINT | 0.0% | 1107158619 | Joins to facilities.id |
| nct_id | VARCHAR | 0.0% | NCT05798845 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 74938306 | Table primary key (auto-increment) |

## id_information

Identifiers other than NCT ID (org study IDs, secondary IDs)

Source file: `id_information.txt`
Rows: 748,312

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| id_link | VARCHAR | 94.6% | https://reporter.nih.gov/quickSearch/U01HL049609 |  |
| id_type_description | VARCHAR | 89.3% | NCI |  |
| id_type | VARCHAR | 81.3% | NIH |  |
| id_value | VARCHAR | 0.0% | U01HL049609 |  |
| id_source | VARCHAR | 0.0% | secondary_id |  |
| nct_id | VARCHAR | 0.0% | NCT00005500 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 236018261 | Table primary key (auto-increment) |

## intervention_other_names

Synonymous names for interventions

Source file: `intervention_other_names.txt`
Rows: 470,456

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| name | VARCHAR | 0.0% | Imfinzi |  |
| intervention_id | BIGINT | 0.0% | 307651967 | Joins to interventions.id |
| nct_id | VARCHAR | 0.0% | NCT04462328 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 152972322 | Table primary key (auto-increment) |

## interventions

Interventions or exposures: drugs, devices, procedures, vaccines

Source file: `interventions.txt`
Rows: 973,952

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 9.4% | During AIH, the participant will be equipped with a non-rebreathing face mask... |  |
| name | VARCHAR | 0.0% | Acute Intermittent Hypoxia |  |
| intervention_type | VARCHAR | 0.0% | OTHER |  |
| nct_id | VARCHAR | 0.0% | NCT06413602 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 307055137 | Table primary key (auto-increment) |

## ipd_information_types

Individual participant data sharing information types

Source file: `ipd_information_types.txt`
Rows: 87,849

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| name | VARCHAR | 0.0% | STUDY_PROTOCOL |  |
| nct_id | VARCHAR | 0.0% | NCT03064763 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 25773130 | Table primary key (auto-increment) |

## keywords

Investigator-provided keywords describing the study

Source file: `keywords.txt`
Rows: 1,523,516

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| downcase_name | VARCHAR | 0.0% | reconstructive surgery |  |
| name | VARCHAR | 0.0% | reconstructive surgery |  |
| nct_id | VARCHAR | 0.0% | NCT02439047 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 474051909 | Table primary key (auto-increment) |

## links

Web links relevant to the study

Source file: `links.txt`
Rows: 74,921

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 0.0% | NIH Clinical Center Detailed Web Page |  |
| url | VARCHAR | 0.0% | https://clinicalstudies.info.nih.gov/cgi/detail.cgi?B_2010-HG-0076.html |  |
| nct_id | VARCHAR | 0.0% | NCT01087346 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 23706577 | Table primary key (auto-increment) |

## milestones

Participant progress through each stage of the study

Source file: `milestones.txt`
Rows: 855,865

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| count_units | BIGINT | 98.1% | 53 |  |
| milestone_description | VARCHAR | 96.7% | Patients treated until progression |  |
| count | BIGINT | 0.0% | 120 |  |
| description | VARCHAR | 100.0% |  |  |
| period | VARCHAR | 0.0% | Overall Study |  |
| title | VARCHAR | 0.0% | STARTED |  |
| ctgov_group_code | VARCHAR | 0.0% | FG000 |  |
| result_group_id | BIGINT | 0.0% | 649733689 | Joins to result_groups.id |
| nct_id | VARCHAR | 0.0% | NCT01298570 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 264071091 | Table primary key (auto-increment) |

## outcome_analyses

Statistical analyses performed on outcomes

Source file: `outcome_analyses.txt`
Rows: 315,026

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| p_value_raw | VARCHAR | 18.4% | .495 |  |
| ci_lower_limit_raw | VARCHAR | 36.4% | -2.46 |  |
| ci_upper_limit_raw | DOUBLE | 36.5% | 1.92 |  |
| other_analysis_description | VARCHAR | 98.9% | A series of generalized linear mixed-effect models were implemented to predic... |  |
| groups_description | VARCHAR | 41.7% | Comparison of mean weight gain between groups. |  |
| estimate_description | VARCHAR | 78.1% | Hazard ratio was estimated using stratified proportional hazards model with A... |  |
| method_description | VARCHAR | 80.9% | p-values have been calculated using logistic regression with factors for trea... |  |
| method | VARCHAR | 14.8% | t-test, 2 sided |  |
| p_value_description | VARCHAR | 71.6% | Threshold of significance is p\<.05 |  |
| ci_upper_limit_na_comment | VARCHAR | 100.0% | Maximum likelihood estimate does not exist |  |
| ci_upper_limit | DOUBLE | 36.5% | 1.92 |  |
| ci_lower_limit | DOUBLE | 36.4% | -2.46 |  |
| ci_percent | DOUBLE | 30.3% | 95.0 |  |
| ci_n_sides | VARCHAR | 32.7% | TWO_SIDED |  |
| p_value | DOUBLE | 18.4% | 0.495 |  |
| p_value_modifier | VARCHAR | 79.6% | < |  |
| dispersion_value | DOUBLE | 81.3% | 0.059 |  |
| dispersion_type | VARCHAR | 81.3% | STANDARD_DEVIATION |  |
| param_value | DOUBLE | 31.1% | 1.063 |  |
| param_type | VARCHAR | 31.1% | Ratio |  |
| non_inferiority_description | VARCHAR | 86.1% | Test of equality (any treatment difference) |  |
| non_inferiority_type | VARCHAR | 0.0% | OTHER |  |
| outcome_id | BIGINT | 0.0% | 202144117 | Joins to outcomes.id |
| nct_id | VARCHAR | 0.0% | NCT00746252 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 101025103 | Table primary key (auto-increment) |

## outcome_analysis_groups

Groups involved in each outcome analysis

Source file: `outcome_analysis_groups.txt`
Rows: 609,509

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| ctgov_group_code | VARCHAR | 0.0% | OG000 |  |
| result_group_id | BIGINT | 0.0% | 650509446 | Joins to result_groups.id |
| outcome_analysis_id | BIGINT | 0.0% | 100888301 | Joins to outcome_analyses.id |
| nct_id | VARCHAR | 0.0% | NCT01972217 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 195529397 | Table primary key (auto-increment) |

## outcome_counts

Sample sizes for each outcome by study group

Source file: `outcome_counts.txt`
Rows: 1,537,817

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| count | BIGINT | 0.0% | 0 |  |
| units | VARCHAR | 0.0% | Participants |  |
| scope | VARCHAR | 0.0% | Measure |  |
| ctgov_group_code | VARCHAR | 0.0% | OG001 |  |
| result_group_id | BIGINT | 0.0% | 651015310 | Joins to result_groups.id |
| outcome_id | BIGINT | 0.0% | 202007061 | Joins to outcomes.id |
| nct_id | VARCHAR | 0.0% | NCT02126878 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 485449530 | Table primary key (auto-increment) |

## outcome_measurements

Summary data for outcome measures by study group

Source file: `outcome_measurements.txt`
Rows: 4,777,352

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| dispersion_lower_limit_raw | VARCHAR | 82.7% | 12.26 |  |
| dispersion_upper_limit_raw | VARCHAR | 82.7% | 15.59 |  |
| explanation_of_na | VARCHAR | 98.0% | Mean and standard deviation do not apply for zero participants. |  |
| dispersion_upper_limit | DOUBLE | 83.4% | 15.59 |  |
| dispersion_lower_limit | DOUBLE | 83.1% | 12.26 |  |
| dispersion_value_num | DOUBLE | 64.8% | 0.61 |  |
| dispersion_value | VARCHAR | 63.7% | 0.61 |  |
| dispersion_type | VARCHAR | 46.8% | Standard Deviation |  |
| param_value_num | DOUBLE | 1.1% | 0.0 |  |
| param_value | VARCHAR | 0.0% | 0 |  |
| param_type | VARCHAR | 0.0% | COUNT_OF_PARTICIPANTS |  |
| units | VARCHAR | 0.0% | Participants |  |
| description | VARCHAR | 4.6% | Respiratory/Miscellaneous AE include any respiratory/miscellaneous AE, conjun... |  |
| title | VARCHAR | 0.0% | Number of Subjects Reporting EMA Defined AEIs (Respiratory/Miscellaneous Adve... |  |
| category | VARCHAR | 93.1% | Normal |  |
| classification | VARCHAR | 19.7% | Any, Week 37 |  |
| ctgov_group_code | VARCHAR | 0.0% | OG000 |  |
| result_group_id | BIGINT | 0.0% | 650765031 | Joins to result_groups.id |
| outcome_id | BIGINT | 0.0% | 201932261 | Joins to outcomes.id |
| nct_id | VARCHAR | 0.0% | NCT02893878 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 1502764961 | Table primary key (auto-increment) |

## outcomes

Outcome measure descriptions and time frames

Source file: `outcomes.txt`
Rows: 638,016

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| param_type | VARCHAR | 7.3% | COUNT_OF_UNITS |  |
| dispersion_type | VARCHAR | 39.4% | Standard Deviation |  |
| units_analyzed | VARCHAR | 98.0% | Treatment Areas |  |
| units | VARCHAR | 7.3% | Treatment Areas |  |
| anticipated_posting_month_year | VARCHAR | 99.0% | 2025-11 |  |
| anticipated_posting_date | DATE | 99.0% | 2025-11-01 |  |
| population | VARCHAR | 24.6% | Per protocol |  |
| time_frame | VARCHAR | 0.0% | Prior to or at 8 weeks |  |
| description | VARCHAR | 7.5% | The incidence of healing is hypothesized to be non-inferior for RECELL-treate... |  |
| title | VARCHAR | 0.0% | Incidence of Treatment Area Healing |  |
| outcome_type | VARCHAR | 0.0% | PRIMARY |  |
| nct_id | VARCHAR | 0.0% | NCT04091672 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 201998104 | Table primary key (auto-increment) |

## overall_officials

People responsible for overall scientific leadership

Source file: `overall_officials.txt`
Rows: 519,601

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| affiliation | VARCHAR | 0.5% | Wake Forest University Health Sciences |  |
| name | VARCHAR | 0.0% | Philip J Brown, PhD |  |
| role | VARCHAR | 0.3% | PRINCIPAL_INVESTIGATOR |  |
| nct_id | VARCHAR | 0.0% | NCT04733677 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 167727855 | Table primary key (auto-increment) |

## participant_flows

Recruitment and pre-assignment details

Source file: `participant_flows.txt`
Rows: 76,963

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| units_analyzed | VARCHAR | 98.3% | Village cluster |  |
| pre_assignment_details | VARCHAR | 61.2% | All patients were screened for eligibility to participate in the trial. Patie... |  |
| recruitment_details | VARCHAR | 59.7% | There were 942 participants (468 received placebo and 474 received dexpramipe... |  |
| nct_id | VARCHAR | 0.0% | NCT01818986 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 23982765 | Table primary key (auto-increment) |

## pending_results

Events related to submission of results for QC review

Source file: `pending_results.txt`
Rows: 32,304

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| event_date | DATE | 1.3% | 2022-09-01 |  |
| event_date_description | DATE | 1.3% | 2022-09-01 |  |
| event | VARCHAR | 0.0% | RELEASE |  |
| nct_id | VARCHAR | 0.0% | NCT05333315 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 10298013 | Table primary key (auto-increment) |

## provided_documents

Protocol, SAP, and informed consent form documents

Source file: `provided_documents.txt`
Rows: 78,018

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| url | VARCHAR | 0.0% | https://ClinicalTrials.gov/ProvidedDocs/51/NCT02592551/Prot_SAP_000.pdf |  |
| document_date | DATE | 0.0% | 2019-04-17 |  |
| has_sap | BOOLEAN | 0.0% | true |  |
| has_icf | BOOLEAN | 0.0% | false |  |
| has_protocol | BOOLEAN | 0.0% | true |  |
| document_type | VARCHAR | 0.0% | Study Protocol and Statistical Analysis Plan |  |
| nct_id | VARCHAR | 0.0% | NCT02592551 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 22432460 | Table primary key (auto-increment) |

## reported_event_totals

Totals of reported adverse events by category

Source file: `reported_event_totals.txt`
Rows: 577,536

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| updated_at | TIMESTAMP | 0.0% | 2026-03-15 05:50:58.00926 |  |
| created_at | TIMESTAMP | 0.0% | 2026-03-15 05:50:58.00926 |  |
| subjects_at_risk | BIGINT | 12.5% | 11 |  |
| subjects_affected | BIGINT | 12.3% | 11 |  |
| classification | VARCHAR | 0.0% | Total, all-cause mortality |  |
| event_type | VARCHAR | 0.0% | deaths |  |
| ctgov_group_code | VARCHAR | 0.0% | EG000 |  |
| nct_id | VARCHAR | 0.0% | NCT01253642 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 178794688 | Table primary key (auto-increment) |

## reported_events

Summary of reported adverse events

Source file: `reported_events.txt`
Rows: 11,446,277

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| assessment | VARCHAR | 2.2% | SYSTEMATIC_ASSESSMENT |  |
| vocab | VARCHAR | 10.9% | MedDRA (25.0) |  |
| frequency_threshold | BIGINT | 0.0% | 5 |  |
| adverse_event_term | VARCHAR | 0.0% | Rash maculo-papular |  |
| organ_system | VARCHAR | 0.0% | Skin and subcutaneous tissue disorders |  |
| event_count | BIGINT | 56.6% | 1 |  |
| description | VARCHAR | 33.4% | Any sign or symptom that occurs during the conduct of the trial and safety fo... |  |
| subjects_at_risk | BIGINT | 0.0% | 3 |  |
| subjects_affected | BIGINT | 0.8% | 0 |  |
| default_assessment | VARCHAR | 100.0% |  |  |
| default_vocab | VARCHAR | 100.0% |  |  |
| event_type | VARCHAR | 0.0% | other |  |
| time_frame | VARCHAR | 12.5% | Adverse events were collected from first dose of study treatment to 30 days a... |  |
| ctgov_group_code | VARCHAR | 0.0% | EG004 |  |
| result_group_id | BIGINT | 0.0% | 650191975 | Joins to result_groups.id |
| nct_id | VARCHAR | 0.0% | NCT02335944 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 1359228140 | Table primary key (auto-increment) |

## responsible_parties

Parties responsible for submitting study information

Source file: `responsible_parties.txt`
Rows: 557,553

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| old_name_title | VARCHAR | 95.5% | George S. Alexopoulos, M.D. |  |
| affiliation | VARCHAR | 57.4% | Air Force Military Medical University, China |  |
| organization | VARCHAR | 95.5% | Weill Medical College of Cornell University |  |
| title | VARCHAR | 57.4% | Associate professor |  |
| name | VARCHAR | 57.4% | Zhihong LU |  |
| responsible_party_type | VARCHAR | 4.6% | SPONSOR |  |
| nct_id | VARCHAR | 0.0% | NCT06347146 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 179273690 | Table primary key (auto-increment) |

## result_agreements

Agreements between sponsor and principal investigators about results

Source file: `result_agreements.txt`
Rows: 76,963

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| restrictive_agreement | BOOLEAN | 23.0% | false |  |
| other_details | VARCHAR | 72.2% | The Study being conducted under this Agreement is part of the Overall Study. ... |  |
| restriction_type | VARCHAR | 61.5% | OTHER |  |
| agreement | VARCHAR | 100.0% |  |  |
| pi_employee | BOOLEAN | 0.0% | false |  |
| nct_id | VARCHAR | 0.0% | NCT05487300 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 24536089 | Table primary key (auto-increment) |

## result_contacts

Points of contact for scientific information about results

Source file: `result_contacts.txt`
Rows: 76,963

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| extension | VARCHAR | 94.6% | 930 |  |
| email | VARCHAR | 6.3% | linkova@biocad.ru |  |
| phone | VARCHAR | 4.7% | +7 (495) 992 66 28 |  |
| name | VARCHAR | 0.0% | Yulia Linkova Medical Director |  |
| organization | VARCHAR | 0.0% | Biocad |  |
| nct_id | VARCHAR | 0.0% | NCT02762799 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 24474798 | Table primary key (auto-increment) |

## result_groups

Aggregate list of group titles/descriptions for results reporting

Source file: `result_groups.txt`
Rows: 2,120,694

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| outcome_id | BIGINT | 28.7% | 201599192 | Joins to outcomes.id |
| description | VARCHAR | 0.9% | Patients were administered weekly 30mg/m2 of vinorelbine as a short IV infusi... |  |
| title | VARCHAR | 0.0% | Normal |  |
| result_type | VARCHAR | 0.0% | Outcome |  |
| ctgov_group_code | VARCHAR | 0.0% | OG000 |  |
| nct_id | VARCHAR | 0.0% | NCT00540982 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 649658692 | Table primary key (auto-increment) |

## retractions

Retraction notices for study results or publications

Source file: `retractions.txt`
Rows: 334

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| nct_id | VARCHAR | 0.0% | NCT03036293 | Primary trial identifier, joins across all AACT tables |
| source | VARCHAR | 0.0% | Sci Rep. 2022 Sep 14;12(1):15416 |  |
| pmid | BIGINT | 0.0% | 36104393 |  |
| reference_id | BIGINT | 0.0% | 334716747 |  |
| id | BIGINT | 0.0% | 111537 | Table primary key (auto-increment) |

## search_results

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| id | VARCHAR | nan% |  | Table primary key (auto-increment) |
| nct_id | VARCHAR | nan% |  | Primary trial identifier, joins across all AACT tables |
| name | VARCHAR | nan% |  |  |
| created_at | VARCHAR | nan% |  |  |
| updated_at | VARCHAR | nan% |  |  |
| grouping | VARCHAR | nan% |  |  |
| study_search_id | VARCHAR | nan% |  |  |

## search_term_results

Source file: `search_term_results.txt`
Rows: 494,618

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| updated_at | TIMESTAMP | 0.0% | 2026-03-16 04:28:08.969622 |  |
| created_at | TIMESTAMP | 0.0% | 2026-03-16 04:28:08.969535 |  |
| search_term_id | BIGINT | 0.0% | 45 |  |
| nct_id | VARCHAR | 0.0% | NCT00001575 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 195401226 | Table primary key (auto-increment) |

## search_terms

Source file: `search_terms.txt`
Rows: 186

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| updated_at | TIMESTAMP | 0.0% | 2025-01-28 21:03:58.475729 |  |
| created_at | TIMESTAMP | 0.0% | 2025-01-28 21:03:58.475729 |  |
| group | VARCHAR | 0.0% | diseases of the heart |  |
| term | VARCHAR | 0.0% | rheumatic fever without mention of heart involvement |  |
| id | BIGINT | 0.0% | 1 | Table primary key (auto-increment) |

## sponsors

Sponsor and collaborator names and types

Source file: `sponsors.txt`
Rows: 920,618

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| name | VARCHAR | 0.0% | Qilu Pharmaceutical Co., Ltd. |  |
| lead_or_collaborator | VARCHAR | 0.0% | collaborator |  |
| agency_class | VARCHAR | 0.1% | INDUSTRY |  |
| nct_id | VARCHAR | 0.0% | NCT06954116 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 297589735 | Table primary key (auto-increment) |

## studies

Core study record: title, status, phase, type, dates, enrollment, and regulatory info

Source file: `studies.txt`
Rows: 576,029

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| patient_registry | BOOLEAN | 81.0% | false |  |
| baseline_type_units_analyzed | VARCHAR | 99.9% | Teeth |  |
| fdaaa801_violation | VARCHAR | 100.0% | t |  |
| expanded_access_status_for_nctid | VARCHAR | 99.9% | NO_LONGER_AVAILABLE |  |
| expanded_access_nctid | VARCHAR | 99.9% | NCT00046345 |  |
| delayed_posting | BOOLEAN | 99.8% | true |  |
| source_class | VARCHAR | 0.2% | OTHER |  |
| updated_at | TIMESTAMP | 0.0% | 2026-03-14 19:31:10.502755 |  |
| created_at | TIMESTAMP | 0.0% | 2026-03-14 19:31:10.502755 |  |
| plan_to_share_ipd_description | VARCHAR | 85.9% | Individual participant data (IPD) from this trial will be shared with the sci... |  |
| plan_to_share_ipd | VARCHAR | 48.4% | YES |  |
| ipd_url | VARCHAR | 97.8% | https://nda.nih.gov/ |  |
| ipd_access_criteria | VARCHAR | 95.2% | There is no plan to restrict access to anonymized data for research purposes.... |  |
| ipd_time_frame | VARCHAR | 94.7% | De-identified individual participant data (IPD) will be submitted to the NIMH... |  |
| biospec_description | VARCHAR | 95.3% | Epileptogenic and para-epileptogenic tissues from DRE patients and normal tis... |  |
| biospec_retention | VARCHAR | 95.3% | SAMPLES_WITHOUT_DNA |  |
| is_us_export | BOOLEAN | 86.2% | false |  |
| is_ppsd | VARCHAR | 100.0% | t |  |
| is_unapproved_device | BOOLEAN | 99.2% | true |  |
| is_fda_regulated_device | BOOLEAN | 38.8% | false |  |
| is_fda_regulated_drug | BOOLEAN | 38.8% | false |  |
| has_dmc | BOOLEAN | 17.7% | false |  |
| expanded_access_type_treatment | BOOLEAN | 100.0% | true |  |
| expanded_access_type_intermediate | BOOLEAN | 100.0% | true |  |
| expanded_access_type_individual | BOOLEAN | 99.9% | true |  |
| has_expanded_access | BOOLEAN | 1.2% | false |  |
| why_stopped | VARCHAR | 92.2% | Business Decision |  |
| number_of_groups | BIGINT | 84.7% | 2 |  |
| number_of_arms | BIGINT | 27.8% | 3 |  |
| limitations_and_caveats | VARCHAR | 97.2% | The sponsor made the decision to not continue the study at the end of Part 1 ... |  |
| source | VARCHAR | 0.0% | University of Pittsburgh |  |
| enrollment_type | VARCHAR | 3.0% | ACTUAL |  |
| enrollment | BIGINT | 1.2% | 45 |  |
| phase | VARCHAR | 23.7% | PHASE1 |  |
| last_known_status | VARCHAR | 84.4% | ACTIVE_NOT_RECRUITING |  |
| overall_status | VARCHAR | 0.0% | COMPLETED |  |
| official_title | VARCHAR | 1.7% | A Phase I Study to Evaluate the Safety and Pharmacokinetics of S-CKD602 in Pa... |  |
| brief_title | VARCHAR | 0.0% | Safety Study of S-CKD602 in Patients With Advanced Malignancies |  |
| baseline_population | VARCHAR | 95.6% | The sponsor made the decision to not continue the study at the end of Part 1 ... |  |
| acronym | VARCHAR | 71.4% | REPERFUSE |  |
| study_type | VARCHAR | 0.2% | INTERVENTIONAL |  |
| target_duration | VARCHAR | 97.2% | 60 Days |  |
| primary_completion_date | DATE | 3.8% | 2006-05-31 |  |
| primary_completion_date_type | DATE | 100.0% |  |  |
| primary_completion_month_year | VARCHAR | 3.8% | 2006-05 |  |
| completion_date | DATE | 2.9% | 2006-05-31 |  |
| completion_date_type | DATE | 100.0% |  |  |
| completion_month_year | VARCHAR | 2.9% | 2006-05 |  |
| verification_date | DATE | 0.2% | 2013-12-31 |  |
| verification_month_year | VARCHAR | 0.2% | 2013-12 |  |
| start_date | DATE | 0.9% | 2003-09-30 |  |
| start_date_type | DATE | 100.0% |  |  |
| start_month_year | VARCHAR | 0.9% | 2003-09 |  |
| last_update_posted_date_type | DATE | 100.0% |  |  |
| last_update_posted_date | DATE | 0.0% | 2013-12-19 |  |
| last_update_submitted_qc_date | DATE | 0.0% | 2013-12-18 |  |
| disposition_first_posted_date_type | DATE | 100.0% |  |  |
| disposition_first_posted_date | DATE | 98.3% | 2010-12-06 |  |
| disposition_first_submitted_qc_date | DATE | 98.6% | 2010-12-02 |  |
| results_first_posted_date_type | DATE | 100.0% |  |  |
| results_first_posted_date | DATE | 86.6% | 2019-06-03 |  |
| results_first_submitted_qc_date | DATE | 86.6% | 2019-02-25 |  |
| study_first_posted_date_type | DATE | 100.0% |  |  |
| study_first_posted_date | DATE | 0.0% | 2005-09-15 |  |
| study_first_submitted_qc_date | DATE | 0.0% | 2005-09-12 |  |
| last_update_submitted_date | DATE | 0.0% | 2013-12-18 |  |
| disposition_first_submitted_date | DATE | 98.3% | 2010-10-16 |  |
| results_first_submitted_date | DATE | 86.6% | 2018-09-24 |  |
| study_first_submitted_date | DATE | 0.0% | 2005-09-12 |  |
| nlm_download_date_description | VARCHAR | 100.0% |  |  |
| nct_id | VARCHAR | 0.0% | NCT00177281 | Primary trial identifier, joins across all AACT tables |

## study_references

Citations to publications related to the study

Source file: `study_references.txt`
Rows: 1,078,399

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| citation | VARCHAR | 0.0% | Sica D, Gradman AH, Lederballe O, Kolloch RE, Zhang J, Keefe DL. Long-term sa... |  |
| reference_type | VARCHAR | 0.0% | DERIVED |  |
| pmid | BIGINT | 5.2% | 22035463 |  |
| nct_id | VARCHAR | 0.0% | NCT00219037 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 334152515 | Table primary key (auto-increment) |
