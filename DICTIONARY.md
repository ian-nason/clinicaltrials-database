# Data Dictionary

Source: [AACT (Aggregate Analysis of ClinicalTrials.gov)](https://aact.ctti-clinicaltrials.org/)

## baseline_counts

Sample sizes at baseline for each study group

Source file: `baseline_counts.txt`
Rows: 236,718

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| count | BIGINT | 0.0% | 58 |  |
| scope | VARCHAR | 0.0% | overall |  |
| units | VARCHAR | 0.0% | Participants |  |
| ctgov_group_code | VARCHAR | 0.0% | BG000 |  |
| result_group_id | BIGINT | 0.0% | 772179886 | Joins to result_groups.id |
| nct_id | VARCHAR | 0.0% | NCT04311502 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 86088074 | Table primary key (auto-increment) |

## baseline_measurements

Demographic and baseline measures by group

Source file: `baseline_measurements.txt`
Rows: 2,905,943

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| calculate_percentage | BOOLEAN | 96.6% | false |  |
| population_description | VARCHAR | 94.4% | Race and Ethnicity were not collected from any participant. |  |
| number_analyzed_units | VARCHAR | 0.0% | Participants |  |
| number_analyzed | BIGINT | 0.1% | 6 |  |
| explanation_of_na | VARCHAR | 99.8% | Standard deviation cannot be calculated for a single participant. |  |
| dispersion_upper_limit | DOUBLE | 97.8% | 19.0 |  |
| dispersion_lower_limit | DOUBLE | 97.8% | 1.0 |  |
| dispersion_value_num | DOUBLE | 89.3% | 6.4 |  |
| dispersion_value | VARCHAR | 89.2% | 6.40 |  |
| dispersion_type | VARCHAR | 87.0% | STANDARD_DEVIATION |  |
| param_value_num | DOUBLE | 0.3% | 29.81 |  |
| param_value | VARCHAR | 0.1% | 29.81 |  |
| param_type | VARCHAR | 0.0% | MEAN |  |
| units | VARCHAR | 0.0% | years |  |
| description | VARCHAR | 90.3% | The TWEAK alcohol screening test is a short, five-question test that was orig... |  |
| title | VARCHAR | 0.0% | Age, Continuous |  |
| category | VARCHAR | 35.6% | Female |  |
| classification | VARCHAR | 74.5% | United States |  |
| ctgov_group_code | VARCHAR | 0.1% | BG000 |  |
| result_group_id | BIGINT | 0.1% | 771502978 | Joins to result_groups.id |
| nct_id | VARCHAR | 0.0% | NCT02602288 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 1014065240 | Table primary key (auto-increment) |

## brief_summaries

Brief text summary of the study protocol

Source file: `brief_summaries.txt`
Rows: 591,233

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 0.0% | In this proposed study, tACS will be used to intervene in the autism spectrum... |  |
| nct_id | VARCHAR | 0.0% | NCT06362200 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 213977433 | Table primary key (auto-increment) |

## browse_conditions

NLM-generated MeSH terms for study conditions

Source file: `browse_conditions.txt`
Rows: 4,300,046

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| mesh_type | VARCHAR | 0.0% | mesh-ancestor |  |
| downcase_mesh_term | VARCHAR | 0.0% | bronchial diseases |  |
| mesh_term | VARCHAR | 0.0% | Bronchial Diseases |  |
| nct_id | VARCHAR | 0.0% | NCT05304039 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 1506974639 | Table primary key (auto-increment) |

## browse_interventions

NLM-generated MeSH terms for study interventions

Source file: `browse_interventions.txt`
Rows: 2,525,611

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| mesh_type | VARCHAR | 0.0% | mesh-ancestor |  |
| downcase_mesh_term | VARCHAR | 0.0% | pregnenediones |  |
| mesh_term | VARCHAR | 0.0% | Pregnenediones |  |
| nct_id | VARCHAR | 0.0% | NCT06209047 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 780714432 | Table primary key (auto-increment) |

## calculated_values

AACT-computed fields: months to report results, facilities count, etc.

Source file: `calculated_values.txt`
Rows: 592,206

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| number_of_other_outcomes_to_measure | BIGINT | 91.5% | 3 |  |
| number_of_secondary_outcomes_to_measure | BIGINT | 27.4% | 8 |  |
| number_of_primary_outcomes_to_measure | BIGINT | 3.0% | 2 |  |
| maximum_age_unit | VARCHAR | 46.9% | year |  |
| minimum_age_unit | VARCHAR | 6.5% | year |  |
| maximum_age_num | BIGINT | 46.9% | 90 |  |
| minimum_age_num | BIGINT | 6.5% | 18 |  |
| has_single_facility | BOOLEAN | 10.1% | true |  |
| has_us_facility | BOOLEAN | 10.1% | false |  |
| months_to_report_results | BIGINT | 86.7% | 20 |  |
| were_results_reported | BOOLEAN | 0.0% | false |  |
| actual_duration | BIGINT | 38.7% | 6 |  |
| nlm_download_date | VARCHAR | 100.0% |  |  |
| registered_in_calendar_year | BIGINT | 0.0% | 2024 |  |
| number_of_sae_subjects | BIGINT | 92.9% | 1 |  |
| number_of_nsae_subjects | BIGINT | 90.8% | 13 |  |
| number_of_facilities | BIGINT | 0.0% | 1 |  |
| nct_id | VARCHAR | 0.0% | NCT06617767 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 237881648 | Table primary key (auto-increment) |

## central_contacts

Primary and backup contacts for enrollment questions

Source file: `central_contacts.txt`
Rows: 222,655

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| role | VARCHAR | 0.0% | CONTACT |  |
| phone_extension | VARCHAR | 88.4% | 1174 |  |
| email | VARCHAR | 2.3% | lavona.traywick@achehealth.edu |  |
| phone | VARCHAR | 6.1% | 4794016023 |  |
| name | VARCHAR | 0.0% | LaVona Traywick, PHD |  |
| contact_type | VARCHAR | 0.0% | primary |  |
| nct_id | VARCHAR | 0.0% | NCT06139549 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 82044148 | Table primary key (auto-increment) |

## conditions

Disease or condition names studied in each trial

Source file: `conditions.txt`
Rows: 1,060,832

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| downcase_name | VARCHAR | 0.0% | moyamoya disease |  |
| name | VARCHAR | 0.0% | Moyamoya Disease |  |
| nct_id | VARCHAR | 0.0% | NCT05860946 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 379282743 | Table primary key (auto-increment) |

## countries

Countries where the study has sites

Source file: `countries.txt`
Rows: 803,708

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| removed | BOOLEAN | 0.0% | true |  |
| name | VARCHAR | 0.0% | United States |  |
| nct_id | VARCHAR | 0.0% | NCT04286087 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 294617749 | Table primary key (auto-increment) |

## design_group_interventions

Cross-reference mapping design groups to interventions

Source file: `design_group_interventions.txt`
Rows: 1,320,148

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| intervention_id | BIGINT | 0.0% | 363869734 | Joins to interventions.id |
| design_group_id | BIGINT | 0.0% | 401596675 | Joins to design_groups.id |
| nct_id | VARCHAR | 0.0% | NCT02704143 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 479378175 | Table primary key (auto-increment) |

## design_groups

Protocol-specified groups or cohorts assigned to interventions

Source file: `design_groups.txt`
Rows: 1,088,089

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 11.8% | Must have a brain tumor, or residual abnormality that is measurable or evalua... |  |
| title | VARCHAR | 0.0% | 1/Patients |  |
| group_type | VARCHAR | 15.4% | EXPERIMENTAL |  |
| nct_id | VARCHAR | 0.0% | NCT00067821 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 401046259 | Table primary key (auto-increment) |

## design_outcomes

Planned outcome measures and observations

Source file: `design_outcomes.txt`
Rows: 3,683,025

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 17.6% | Time to development of claudication for each leg will be determined on an upr... |  |
| population | VARCHAR | 100.0% |  |  |
| time_frame | VARCHAR | 1.4% | 1 month |  |
| measure | VARCHAR | 0.0% | Time to claudication on treadmill exercise test |  |
| outcome_type | VARCHAR | 0.0% | other |  |
| nct_id | VARCHAR | 0.0% | NCT02877563 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 1319200456 | Table primary key (auto-increment) |

## designs

Study design details: allocation, masking, assignment, purpose

Source file: `designs.txt`
Rows: 587,431

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| outcomes_assessor_masked | BOOLEAN | 67.5% | false |  |
| investigator_masked | BOOLEAN | 67.5% | false |  |
| caregiver_masked | BOOLEAN | 67.5% | false |  |
| subject_masked | BOOLEAN | 67.5% | true |  |
| intervention_model_description | VARCHAR | 85.0% | Prospective randomized controlled trial |  |
| masking_description | VARCHAR | 92.3% | Patients will be randomly allocated to either interventional or control group... |  |
| masking | VARCHAR | 24.0% | SINGLE |  |
| time_perspective | VARCHAR | 77.0% | RETROSPECTIVE |  |
| primary_purpose | VARCHAR | 24.2% | TREATMENT |  |
| observational_model | VARCHAR | 77.4% | COHORT |  |
| intervention_model | VARCHAR | 24.2% | PARALLEL |  |
| allocation | VARCHAR | 24.0% | RANDOMIZED |  |
| nct_id | VARCHAR | 0.0% | NCT03779373 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 212669543 | Table primary key (auto-increment) |

## detailed_descriptions

Detailed text description of the study protocol

Source file: `detailed_descriptions.txt`
Rows: 591,233

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 32.7% | Hodgkin Lymphoma (HL) is a hematological neoplasia that mainly affects young ... |  |
| nct_id | VARCHAR | 0.0% | NCT02695251 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 214238006 | Table primary key (auto-increment) |

## documents

Full study protocol and statistical analysis plan

Source file: `documents.txt`
Rows: 10,804

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| comment | VARCHAR | 13.7% | Select individual patient-level data from this trial can be requested from th... |  |
| url | VARCHAR | 0.0% | https://nctn-data-archive.nci.nih.gov/ |  |
| document_type | VARCHAR | 0.0% | Individual Participant Data Set |  |
| document_id | VARCHAR | 15.3% | NCT00567580 | Joins to documents.id |
| nct_id | VARCHAR | 0.0% | NCT00567580 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 4119948 | Table primary key (auto-increment) |

## drop_withdrawals

Summary of participant withdrawals: counts and reasons

Source file: `drop_withdrawals.txt`
Rows: 594,116

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| count_units | VARCHAR | 100.0% |  |  |
| reason_comment | VARCHAR | 100.0% |  |  |
| drop_withdraw_comment | VARCHAR | 100.0% |  |  |
| count | BIGINT | 0.0% | 2 |  |
| reason | VARCHAR | 0.0% | Adverse Event |  |
| period | VARCHAR | 0.0% | Overall Study |  |
| ctgov_group_code | VARCHAR | 0.0% | FG000 |  |
| result_group_id | BIGINT | 0.0% | 772372495 | Joins to result_groups.id |
| nct_id | VARCHAR | 0.0% | NCT01594749 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 213112552 | Table primary key (auto-increment) |

## eligibilities

Participant eligibility criteria (inclusion/exclusion, age, sex)

Source file: `eligibilities.txt`
Rows: 591,233

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| older_adult | BOOLEAN | 0.0% | true |  |
| child | BOOLEAN | 0.0% | false |  |
| adult | BOOLEAN | 0.0% | true |  |
| gender_based | BOOLEAN | 96.7% | true |  |
| gender_description | VARCHAR | 97.9% | Participant identifies as a woman |  |
| criteria | VARCHAR | 0.0% | Inclusion Criteria:~* Patient is able to travel to MRI centers~* All patients... |  |
| population | VARCHAR | 77.3% | Patients will be recruited for the study |  |
| healthy_volunteers | BOOLEAN | 2.3% | false |  |
| maximum_age | VARCHAR | 46.8% | 70 Years |  |
| minimum_age | VARCHAR | 6.4% | 18 Years |  |
| gender | VARCHAR | 0.1% | ALL |  |
| sampling_method | VARCHAR | 77.3% | NON_PROBABILITY_SAMPLE |  |
| nct_id | VARCHAR | 0.0% | NCT01110577 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 214275277 | Table primary key (auto-increment) |

## facilities

Facility names, addresses, and recruiting status

Source file: `facilities.txt`
Rows: 3,480,413

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| longitude | DOUBLE | 2.6% | 4.70093 |  |
| latitude | DOUBLE | 2.6% | 50.87959 |  |
| country | VARCHAR | 0.0% | Belgium |  |
| zip | VARCHAR | 19.1% | 3000 |  |
| state | VARCHAR | 39.2% | Vlaams Brabant |  |
| city | VARCHAR | 0.0% | Leuven |  |
| name | VARCHAR | 6.3% | KU Leuven |  |
| status | VARCHAR | 85.4% | RECRUITING |  |
| nct_id | VARCHAR | 0.0% | NCT06105437 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 1304905275 | Table primary key (auto-increment) |

## facility_contacts

Contact information at each study facility

Source file: `facility_contacts.txt`
Rows: 415,701

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| phone_extension | VARCHAR | 94.4% | +90 |  |
| phone | VARCHAR | 28.0% | 010-67781331 |  |
| email | VARCHAR | 28.2% | dryihebalichi@126.com |  |
| name | VARCHAR | 3.3% | Nikoleta Printza |  |
| contact_type | VARCHAR | 0.0% | primary |  |
| facility_id | BIGINT | 0.0% | 1306517481 | Joins to facilities.id |
| nct_id | VARCHAR | 0.0% | NCT03964701 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 164052272 | Table primary key (auto-increment) |

## facility_investigators

Investigator names at each study facility

Source file: `facility_investigators.txt`
Rows: 225,407

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| name | VARCHAR | 0.0% | Bhagirathbhai Dholaria |  |
| role | VARCHAR | 0.0% | PRINCIPAL_INVESTIGATOR |  |
| facility_id | BIGINT | 0.0% | 1307723621 | Joins to facilities.id |
| nct_id | VARCHAR | 0.0% | NCT07673367 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 88648985 | Table primary key (auto-increment) |

## id_information

Identifiers other than NCT ID (org study IDs, secondary IDs)

Source file: `id_information.txt`
Rows: 768,642

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| id_link | VARCHAR | 94.6% | https://reporter.nih.gov/quickSearch/UL1TR001082 |  |
| id_type_description | VARCHAR | 89.2% | bpums |  |
| id_type | VARCHAR | 81.2% | EUDRACT_NUMBER |  |
| id_value | VARCHAR | 0.0% | 2015-004936-36 |  |
| id_source | VARCHAR | 0.0% | secondary_id |  |
| nct_id | VARCHAR | 0.0% | NCT02950051 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 279325405 | Table primary key (auto-increment) |

## intervention_other_names

Synonymous names for interventions

Source file: `intervention_other_names.txt`
Rows: 480,499

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| name | VARCHAR | 0.0% | CB7630 |  |
| intervention_id | BIGINT | 0.0% | 363408282 | Joins to interventions.id |
| nct_id | VARCHAR | 0.0% | NCT01503229 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 180600555 | Table primary key (auto-increment) |

## interventions

Interventions or exposures: drugs, devices, procedures, vaccines

Source file: `interventions.txt`
Rows: 1,001,441

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 9.1% | Endometrin 100 mg twice a day |  |
| name | VARCHAR | 0.0% | Vaginal tablet Endometrin twice a day |  |
| intervention_type | VARCHAR | 0.0% | DRUG |  |
| nct_id | VARCHAR | 0.0% | NCT01483365 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 363419085 | Table primary key (auto-increment) |

## ipd_information_types

Individual participant data sharing information types

Source file: `ipd_information_types.txt`
Rows: 92,867

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| name | VARCHAR | 0.0% | STUDY_PROTOCOL |  |
| nct_id | VARCHAR | 0.0% | NCT04963179 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 30910389 | Table primary key (auto-increment) |

## keywords

Investigator-provided keywords describing the study

Source file: `keywords.txt`
Rows: 1,580,811

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| downcase_name | VARCHAR | 0.0% | obesity, gastric balloon, botulinum toxin a, intervention |  |
| name | VARCHAR | 0.0% | obesity, gastric balloon, botulinum toxin A, intervention |  |
| nct_id | VARCHAR | 0.0% | NCT05872932 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 561324263 | Table primary key (auto-increment) |

## links

Web links relevant to the study

Source file: `links.txt`
Rows: 75,078

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 0.0% | Samsung Gear VR Headset |  |
| url | VARCHAR | 0.0% | https://www.samsung.com/global/galaxy/gear-vr/ |  |
| nct_id | VARCHAR | 0.0% | NCT05267704 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 28029180 | Table primary key (auto-increment) |

## milestones

Participant progress through each stage of the study

Source file: `milestones.txt`
Rows: 882,651

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| count_units | BIGINT | 98.0% | 164 |  |
| milestone_description | VARCHAR | 96.6% | 14 participants and 58 total psoriatic plaques divided in the 4 groups. |  |
| count | BIGINT | 0.0% | 57 |  |
| description | VARCHAR | 100.0% |  |  |
| period | VARCHAR | 0.0% | Overall Study |  |
| title | VARCHAR | 0.0% | STARTED |  |
| ctgov_group_code | VARCHAR | 0.0% | FG000 |  |
| result_group_id | BIGINT | 0.0% | 773340161 | Joins to result_groups.id |
| nct_id | VARCHAR | 0.0% | NCT01633788 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 314026114 | Table primary key (auto-increment) |

## outcome_analyses

Statistical analyses performed on outcomes

Source file: `outcome_analyses.txt`
Rows: 322,641

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| p_value_raw | VARCHAR | 18.4% | .65 |  |
| ci_lower_limit_raw | VARCHAR | 36.3% | -7.3 |  |
| ci_upper_limit_raw | VARCHAR | 36.4% | 16.6 |  |
| other_analysis_description | VARCHAR | 98.9% | Difference (Any remibrutinib - Placebo) |  |
| groups_description | VARCHAR | 41.6% | GCLM Biomarker analysis. |  |
| estimate_description | VARCHAR | 78.1% | Analysis was performed using an analysis of covariance (ANCOVA) model adjusti... |  |
| method_description | VARCHAR | 81.0% | Screening pain score was the covariate; study center was modeled as a random ... |  |
| method | VARCHAR | 14.9% | Wilcoxon (Mann-Whitney) |  |
| p_value_description | VARCHAR | 71.5% | P-value is purely nominal |  |
| ci_upper_limit_na_comment | VARCHAR | 100.0% | Not Appropriate, upper intervals were not used in the statistical analysis an... |  |
| ci_upper_limit | DOUBLE | 36.4% | 16.6 |  |
| ci_lower_limit | DOUBLE | 36.3% | -7.3 |  |
| ci_percent | DOUBLE | 30.4% | 95.0 |  |
| ci_n_sides | VARCHAR | 32.6% | TWO_SIDED |  |
| p_value | DOUBLE | 18.4% | 0.65 |  |
| p_value_modifier | VARCHAR | 79.6% | > |  |
| dispersion_value | DOUBLE | 81.4% | 0.58 |  |
| dispersion_type | VARCHAR | 81.4% | STANDARD_ERROR_OF_MEAN |  |
| param_value | DOUBLE | 31.0% | 4.6 |  |
| param_type | VARCHAR | 31.0% | Paired difference |  |
| non_inferiority_description | VARCHAR | 85.7% | Asthma exacerbation rates during follow-up between two randomized treatment a... |  |
| non_inferiority_type | VARCHAR | 0.0% | SUPERIORITY |  |
| outcome_id | BIGINT | 0.0% | 238384778 | Joins to outcomes.id |
| nct_id | VARCHAR | 0.0% | NCT01612221 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 118879305 | Table primary key (auto-increment) |

## outcome_analysis_groups

Groups involved in each outcome analysis

Source file: `outcome_analysis_groups.txt`
Rows: 623,989

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| ctgov_group_code | VARCHAR | 0.0% | OG000 |  |
| result_group_id | BIGINT | 0.0% | 771607816 | Joins to result_groups.id |
| outcome_analysis_id | BIGINT | 0.0% | 118837164 | Joins to outcome_analyses.id |
| nct_id | VARCHAR | 0.0% | NCT01462162 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 230250043 | Table primary key (auto-increment) |

## outcome_counts

Sample sizes for each outcome by study group

Source file: `outcome_counts.txt`
Rows: 1,583,371

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| count | BIGINT | 0.0% | 26 |  |
| units | VARCHAR | 0.0% | Participants |  |
| scope | VARCHAR | 0.0% | Measure |  |
| ctgov_group_code | VARCHAR | 0.0% | OG000 |  |
| result_group_id | BIGINT | 0.0% | 771834288 | Joins to result_groups.id |
| outcome_id | BIGINT | 0.0% | 238357229 | Joins to outcomes.id |
| nct_id | VARCHAR | 0.0% | NCT04233216 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 573063968 | Table primary key (auto-increment) |

## outcome_measurements

Summary data for outcome measures by study group

Source file: `outcome_measurements.txt`
Rows: 4,927,392

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| dispersion_lower_limit_raw | VARCHAR | 82.6% | 0 |  |
| dispersion_upper_limit_raw | VARCHAR | 82.7% | 5 |  |
| explanation_of_na | VARCHAR | 98.0% | None of the subjects from the Havrix Groups received a second vaccine dose wi... |  |
| dispersion_upper_limit | DOUBLE | 83.4% | 5.0 |  |
| dispersion_lower_limit | DOUBLE | 83.0% | 0.0 |  |
| dispersion_value_num | DOUBLE | 64.8% | 0.02 |  |
| dispersion_value | VARCHAR | 63.7% | 0.02 |  |
| dispersion_type | VARCHAR | 46.7% | Standard Error |  |
| param_value_num | DOUBLE | 1.1% | 59.0 |  |
| param_value | VARCHAR | 0.0% | 59 |  |
| param_type | VARCHAR | 0.0% | COUNT_OF_PARTICIPANTS |  |
| units | VARCHAR | 0.0% | Participants |  |
| description | VARCHAR | 4.6% | LDA is defined as DAS28-4(CRP) score of \<3.2. DAS28-4 CRP is a composite end... |  |
| title | VARCHAR | 0.0% | Number of Participants With LDA According to DAS28-4 CRP<=3.2 at Months 3, 6,... |  |
| category | VARCHAR | 93.0% | Tofacitinib as Monotherapy |  |
| classification | VARCHAR | 19.7% | Month 3 |  |
| ctgov_group_code | VARCHAR | 0.0% | OG000 |  |
| result_group_id | BIGINT | 0.0% | 773124431 | Joins to result_groups.id |
| outcome_id | BIGINT | 0.0% | 238746122 | Joins to outcomes.id |
| nct_id | VARCHAR | 0.0% | NCT04079920 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 1778720670 | Table primary key (auto-increment) |

## outcomes

Outcome measure descriptions and time frames

Source file: `outcomes.txt`
Rows: 656,300

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| param_type | VARCHAR | 7.3% | MEAN |  |
| dispersion_type | VARCHAR | 39.3% | Standard Deviation |  |
| units_analyzed | VARCHAR | 98.0% | clusters of DHOs |  |
| units | VARCHAR | 7.3% | BSA % |  |
| anticipated_posting_month_year | VARCHAR | 99.0% | 2009-12 |  |
| anticipated_posting_date | DATE | 99.0% | 2009-12-01 |  |
| population | VARCHAR | 24.7% | Intention to treat population was used for primary outcome. |  |
| time_frame | VARCHAR | 0.0% | Baseline, Week 2, Week 4, Week 8 |  |
| description | VARCHAR | 7.4% | Body Surface Area is a measure of how much skin is impacted by psoriasis usin... |  |
| title | VARCHAR | 0.0% | Change in Psoriatic Body Surface Area Compared to Baseline |  |
| outcome_type | VARCHAR | 0.0% | PRIMARY |  |
| nct_id | VARCHAR | 0.0% | NCT06357221 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 238555097 | Table primary key (auto-increment) |

## overall_officials

People responsible for overall scientific leadership

Source file: `overall_officials.txt`
Rows: 528,514

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| affiliation | VARCHAR | 0.5% | University of Iowa |  |
| name | VARCHAR | 0.0% | Yousef Zakharia, MD |  |
| role | VARCHAR | 0.3% | PRINCIPAL_INVESTIGATOR |  |
| nct_id | VARCHAR | 0.0% | NCT03575013 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 197145849 | Table primary key (auto-increment) |

## participant_flows

Recruitment and pre-assignment details

Source file: `participant_flows.txt`
Rows: 78,958

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| units_analyzed | VARCHAR | 98.3% | Families |  |
| pre_assignment_details | VARCHAR | 61.1% | A total of 382 participants were screened, of which 188 were screen failures.... |  |
| recruitment_details | VARCHAR | 59.6% | The study was conducted at 139 study sites in 13 countries: Canada, United St... |  |
| nct_id | VARCHAR | 0.0% | NCT03744910 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 28463585 | Table primary key (auto-increment) |

## pending_results

Events related to submission of results for QC review

Source file: `pending_results.txt`
Rows: 33,146

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| event_date | DATE | 1.2% | 2017-09-25 |  |
| event_date_description | DATE | 1.2% | 2017-09-25 |  |
| event | VARCHAR | 0.0% | RELEASE |  |
| nct_id | VARCHAR | 0.0% | NCT00280423 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 12145099 | Table primary key (auto-increment) |

## provided_documents

Protocol, SAP, and informed consent form documents

Source file: `provided_documents.txt`
Rows: 82,967

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| url | VARCHAR | 0.0% | https://ClinicalTrials.gov/ProvidedDocs/70/NCT04219670/Prot_002.pdf |  |
| document_date | DATE | 0.0% | 2022-09-22 |  |
| has_sap | BOOLEAN | 0.0% | false |  |
| has_icf | BOOLEAN | 0.0% | false |  |
| has_protocol | BOOLEAN | 0.0% | true |  |
| document_type | VARCHAR | 0.0% | Study Protocol |  |
| nct_id | VARCHAR | 0.0% | NCT04219670 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 27010093 | Table primary key (auto-increment) |

## reported_event_totals

Totals of reported adverse events by category

Source file: `reported_event_totals.txt`
Rows: 594,426

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| updated_at | TIMESTAMP | 0.0% | 2026-07-03 09:46:39.850244 |  |
| created_at | TIMESTAMP | 0.0% | 2026-07-03 09:46:39.850244 |  |
| subjects_at_risk | BIGINT | 12.2% | 36 |  |
| subjects_affected | BIGINT | 11.9% | 7 |  |
| classification | VARCHAR | 0.0% | Total, all-cause mortality |  |
| event_type | VARCHAR | 0.0% | deaths |  |
| ctgov_group_code | VARCHAR | 0.0% | EG000 |  |
| nct_id | VARCHAR | 0.0% | NCT03468218 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 212140729 | Table primary key (auto-increment) |

## reported_events

Summary of reported adverse events

Source file: `reported_events.txt`
Rows: 11,828,940

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| assessment | VARCHAR | 2.2% | SYSTEMATIC_ASSESSMENT |  |
| vocab | VARCHAR | 11.0% | MedDRA (23.0) |  |
| frequency_threshold | BIGINT | 0.0% | 0 |  |
| adverse_event_term | VARCHAR | 0.0% | Rash |  |
| organ_system | VARCHAR | 0.0% | Skin and subcutaneous tissue disorders |  |
| event_count | BIGINT | 56.5% | 4 |  |
| description | VARCHAR | 33.0% | The frequency of adverse events. The same event may appear as both an adverse... |  |
| subjects_at_risk | BIGINT | 0.0% | 20 |  |
| subjects_affected | BIGINT | 0.8% | 0 |  |
| default_assessment | VARCHAR | 100.0% |  |  |
| default_vocab | VARCHAR | 100.0% |  |  |
| event_type | VARCHAR | 0.0% | other |  |
| time_frame | VARCHAR | 12.1% | Part 1: From dosing on Day 1 or Day 14 up to 10 days post dose; Part 2: From ... |  |
| ctgov_group_code | VARCHAR | 0.0% | EG009 |  |
| result_group_id | BIGINT | 0.0% | 772570867 | Joins to result_groups.id |
| nct_id | VARCHAR | 0.0% | NCT04147715 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 2023959605 | Table primary key (auto-increment) |

## responsible_parties

Parties responsible for submitting study information

Source file: `responsible_parties.txt`
Rows: 573,757

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| old_name_title | VARCHAR | 95.6% | Assoc. Prof. Colleen Loo |  |
| affiliation | VARCHAR | 57.1% | Gazi University |  |
| organization | VARCHAR | 95.6% | University of NSW |  |
| title | VARCHAR | 57.1% | Research asistant |  |
| name | VARCHAR | 57.1% | İnci Hazal Ayas |  |
| responsible_party_type | VARCHAR | 4.4% | SPONSOR |  |
| nct_id | VARCHAR | 0.0% | NCT01051401 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 211708400 | Table primary key (auto-increment) |

## result_agreements

Agreements between sponsor and principal investigators about results

Source file: `result_agreements.txt`
Rows: 78,958

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| restrictive_agreement | BOOLEAN | 23.3% | false |  |
| other_details | VARCHAR | 72.4% | If an investigator wishes to publish information from the study, a copy of th... |  |
| restriction_type | VARCHAR | 61.9% | OTHER |  |
| agreement | VARCHAR | 100.0% |  |  |
| pi_employee | BOOLEAN | 0.0% | true |  |
| nct_id | VARCHAR | 0.0% | NCT05396014 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 28955970 | Table primary key (auto-increment) |

## result_contacts

Points of contact for scientific information about results

Source file: `result_contacts.txt`
Rows: 78,958

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| extension | VARCHAR | 94.7% | +1 |  |
| email | VARCHAR | 6.1% | clinicaltrials@alexion.com |  |
| phone | VARCHAR | 4.6% | 1-855-752-2356 |  |
| name | VARCHAR | 0.0% | Alexion Pharmaceuticals, Inc. |  |
| organization | VARCHAR | 0.0% | Alexion Pharmaceuticals, Inc. |  |
| nct_id | VARCHAR | 0.0% | NCT04504825 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 28972285 | Table primary key (auto-increment) |

## result_groups

Aggregate list of group titles/descriptions for results reporting

Source file: `result_groups.txt`
Rows: 2,182,830

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| outcome_id | BIGINT | 28.7% | 238857712 | Joins to outcomes.id |
| description | VARCHAR | 0.8% | This group takes either clomiphene or letrozole on cycle days 3-7 and then re... |  |
| title | VARCHAR | 0.0% | Insemination Day Of Positive OPK |  |
| result_type | VARCHAR | 0.0% | Outcome |  |
| ctgov_group_code | VARCHAR | 0.0% | OG000 |  |
| nct_id | VARCHAR | 0.0% | NCT02294773 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 773501688 | Table primary key (auto-increment) |

## retractions

Retraction notices for study results or publications

Source file: `retractions.txt`
Rows: 335

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| nct_id | VARCHAR | 0.0% | NCT00057577 | Primary trial identifier, joins across all AACT tables |
| source | VARCHAR | 0.0% | JAMA Psychiatry. 2016 Jun 1;73(6):639-40 |  |
| pmid | BIGINT | 0.0% | 27097060 |  |
| reference_id | BIGINT | 0.0% | 396962279 |  |
| id | BIGINT | 0.0% | 130470 | Table primary key (auto-increment) |

## search_term_results

Source file: `search_term_results.txt`
Rows: 506,655

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| updated_at | TIMESTAMP | 0.0% | 2026-07-04 04:35:08.018645 |  |
| created_at | TIMESTAMP | 0.0% | 2026-07-04 04:35:08.018614 |  |
| search_term_id | BIGINT | 0.0% | 45 |  |
| nct_id | VARCHAR | 0.0% | NCT00001465 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 250468548 | Table primary key (auto-increment) |

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
Rows: 945,127

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| name | VARCHAR | 0.0% | National Institute of Neurological Disorders and Stroke (NINDS) |  |
| lead_or_collaborator | VARCHAR | 0.0% | collaborator |  |
| agency_class | VARCHAR | 0.1% | NIH |  |
| nct_id | VARCHAR | 0.0% | NCT04874220 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 350137097 | Table primary key (auto-increment) |

## studies

Core study record: title, status, phase, type, dates, enrollment, and regulatory info

Source file: `studies.txt`
Rows: 592,206

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| patient_registry | BOOLEAN | 80.8% | false |  |
| baseline_type_units_analyzed | VARCHAR | 99.9% | lesions |  |
| fdaaa801_violation | VARCHAR | 100.0% | t |  |
| expanded_access_status_for_nctid | VARCHAR | 99.9% | NO_LONGER_AVAILABLE |  |
| expanded_access_nctid | VARCHAR | 99.9% | NCT05225259 |  |
| delayed_posting | BOOLEAN | 99.8% | true |  |
| source_class | VARCHAR | 0.2% | OTHER |  |
| updated_at | TIMESTAMP | 0.0% | 2026-07-02 12:47:06.403798 |  |
| created_at | TIMESTAMP | 0.0% | 2026-07-02 12:47:06.403798 |  |
| plan_to_share_ipd_description | VARCHAR | 85.4% | Novartis is committed to sharing with qualified external researchers, access ... |  |
| plan_to_share_ipd | VARCHAR | 47.6% | NO |  |
| ipd_url | VARCHAR | 97.8% | https://www.amgen.com/datasharing |  |
| ipd_access_criteria | VARCHAR | 95.0% | Since this is a pilot study only summary data will be provided. |  |
| ipd_time_frame | VARCHAR | 94.6% | Once data collection is complete and data analysis has been completed the res... |  |
| biospec_description | VARCHAR | 95.3% | blood, saliva, and nasal samples |  |
| biospec_retention | VARCHAR | 95.3% | SAMPLES_WITH_DNA |  |
| is_us_export | BOOLEAN | 87.3% | false |  |
| is_ppsd | BOOLEAN | 100.0% | true |  |
| is_unapproved_device | BOOLEAN | 99.1% | true |  |
| is_fda_regulated_device | BOOLEAN | 37.8% | false |  |
| is_fda_regulated_drug | BOOLEAN | 37.8% | false |  |
| has_dmc | BOOLEAN | 17.8% | false |  |
| expanded_access_type_treatment | BOOLEAN | 100.0% | true |  |
| expanded_access_type_intermediate | BOOLEAN | 100.0% | true |  |
| expanded_access_type_individual | BOOLEAN | 99.9% | true |  |
| has_expanded_access | BOOLEAN | 1.2% | false |  |
| why_stopped | VARCHAR | 92.2% | does not meet criteria for clinical trial |  |
| number_of_groups | BIGINT | 84.6% | 3 |  |
| number_of_arms | BIGINT | 27.7% | 4 |  |
| limitations_and_caveats | VARCHAR | 97.2% | Due to rounding some percentages will not equal 100% |  |
| source | VARCHAR | 0.0% | Milton S. Hershey Medical Center |  |
| enrollment_type | VARCHAR | 2.9% | ACTUAL |  |
| enrollment | BIGINT | 1.2% | 0 |  |
| phase | VARCHAR | 23.7% | PHASE2 |  |
| last_known_status | VARCHAR | 84.0% | RECRUITING |  |
| overall_status | VARCHAR | 0.0% | WITHDRAWN |  |
| official_title | VARCHAR | 1.7% | Effects of Resistin on Neutrophil Function |  |
| brief_title | VARCHAR | 0.0% | Effects of Resistin on Neutrophil Function |  |
| baseline_population | VARCHAR | 95.5% | Subjects could choose to participate in multiple arms of the trial. Trial arm... |  |
| acronym | VARCHAR | 71.0% | VIBRANT-HD |  |
| study_type | VARCHAR | 0.2% | OBSERVATIONAL |  |
| target_duration | VARCHAR | 97.1% | 1 Day |  |
| primary_completion_date | DATE | 3.7% | 2019-09-01 |  |
| primary_completion_date_type | VARCHAR | 3.7% | ESTIMATED |  |
| primary_completion_month_year | VARCHAR | 3.7% | 2019-09-01 |  |
| completion_date | DATE | 2.8% | 2019-09-01 |  |
| completion_date_type | VARCHAR | 4.0% | ESTIMATED |  |
| completion_month_year | VARCHAR | 2.8% | 2019-09-01 |  |
| verification_date | DATE | 0.2% | 2023-03-31 |  |
| verification_month_year | VARCHAR | 0.2% | 2023-03 |  |
| start_date | DATE | 0.9% | 2018-09-01 |  |
| start_date_type | VARCHAR | 31.5% | ESTIMATED |  |
| start_month_year | VARCHAR | 0.9% | 2018-09-01 |  |
| last_update_posted_date_type | VARCHAR | 0.0% | ACTUAL |  |
| last_update_posted_date | DATE | 0.0% | 2024-12-10 |  |
| last_update_submitted_qc_date | DATE | 0.0% | 2024-12-05 |  |
| disposition_first_posted_date_type | VARCHAR | 98.4% | ESTIMATED |  |
| disposition_first_posted_date | DATE | 98.4% | 2013-01-29 |  |
| disposition_first_submitted_qc_date | DATE | 98.6% | 2013-01-25 |  |
| results_first_posted_date_type | VARCHAR | 86.7% | ACTUAL |  |
| results_first_posted_date | DATE | 86.7% | 2024-11-04 |  |
| results_first_submitted_qc_date | DATE | 86.7% | 2024-10-30 |  |
| study_first_posted_date_type | VARCHAR | 0.0% | ACTUAL |  |
| study_first_posted_date | DATE | 0.0% | 2018-08-13 |  |
| study_first_submitted_qc_date | DATE | 0.0% | 2018-08-09 |  |
| last_update_submitted_date | DATE | 0.0% | 2024-12-05 |  |
| disposition_first_submitted_date | DATE | 98.4% | 2013-01-15 |  |
| results_first_submitted_date | DATE | 86.7% | 2024-08-27 |  |
| study_first_submitted_date | DATE | 0.0% | 2018-08-03 |  |
| nlm_download_date_description | VARCHAR | 100.0% |  |  |
| nct_id | VARCHAR | 0.0% | NCT03626870 | Primary trial identifier, joins across all AACT tables |

## study_references

Citations to publications related to the study

Source file: `study_references.txt`
Rows: 1,117,973

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| citation | VARCHAR | 0.0% | Wilkins JJ, Savic RM, Karlsson MO, Langdon G, McIlleron H, Pillai G, Smith PJ... |  |
| reference_type | VARCHAR | 0.0% | BACKGROUND |  |
| pmid | BIGINT | 5.1% | 18391026 |  |
| nct_id | VARCHAR | 0.0% | NCT02534727 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 396356638 | Table primary key (auto-increment) |
