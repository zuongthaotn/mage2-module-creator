<?php
namespace {{namespace}}\{{module_name}}\Api;

/**
 * CRUD interface.
 * @api
 * @since 100.0.2
 */
interface {{interface_name}}RepositoryInterface
{
    /**
     * Save {{interface_name_lower}}.
     *
     * @param \{{namespace}}\{{module_name}}\Api\Data\{{interface_name}}Interface ${{interface_name_lower}}
     * @return \{{namespace}}\{{module_name}}\Api\Data\{{interface_name}}Interface
     * @throws \Magento\Framework\Exception\LocalizedException
     */
    public function save(Data\{{interface_name}}Interface ${{interface_name_lower}});

    /**
     * Retrieve {{interface_name_lower}}.
     *
     * @param string ${{interface_name_lower}}Id
     * @return \{{namespace}}\{{module_name}}\Api\Data\{{interface_name}}Interface
     * @throws \Magento\Framework\Exception\LocalizedException
     */
    public function getById(${{interface_name_lower}}Id);

    /**
     * Retrieve {{interface_name_lower}}s matching the specified criteria.
     *
     * @param \Magento\Framework\Api\SearchCriteriaInterface $searchCriteria
     * @return \{{namespace}}\{{module_name}}\Api\Data\{{interface_name}}SearchResultsInterface
     * @throws \Magento\Framework\Exception\LocalizedException
     */
    public function getList(\Magento\Framework\Api\SearchCriteriaInterface $searchCriteria);

    /**
     * Delete {{interface_name_lower}}.
     *
     * @param \{{namespace}}\{{module_name}}\Api\Data\{{interface_name}}Interface ${{interface_name_lower}}
     * @return bool true on success
     * @throws \Magento\Framework\Exception\LocalizedException
     */
    public function delete(Data\{{interface_name}}Interface ${{interface_name_lower}});

    /**
     * Delete {{interface_name_lower}} by ID.
     *
     * @param string ${{interface_name_lower}}Id
     * @return bool true on success
     * @throws \Magento\Framework\Exception\NoSuchEntityException
     * @throws \Magento\Framework\Exception\LocalizedException
     */
    public function deleteById(${{interface_name_lower}}Id);
}
